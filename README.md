# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A submission is sent as JSON to `POST /submit`.
2. The route extracts the `text` and `creator_id` fields to identify the
   writing and its submitter.
3. The model signal analyzes perplexity, or how predictable the writing is to
   the language model.
4. The style signal analyzes patterns in the text, including sentence-length
   variation, vocabulary repetition, and punctuation.
5. The two signal scores are combined into one score.
6. The combined score is used to produce a `human`, `unsure`, or `ai` result
   and a reader-facing label.
7. The decision is written to `logs/audit.jsonl` with its timestamp,
   `content_id`, `creator_id`, guess, model score, style score, combined score,
   label, and status.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
This signal measures perplexity. It measures how predictable the next likely word is against a model that chooses and compares words based on the text given. 

**Why that might differ between human and AI writing:**
Human writing can be more odd, and can change suddenly since it can be unpredictable. Things like odd choices of words and abrupt turns are more common in human writing.

**What it can't see:**
Its blind spot would be towards more simple and plain human writing, because it is more predictable.


### Signal two — the style signal

**What it measures:**
This signal measures the text based on how long the sentences are, the vocabulary repetition, and punctuation.

**Why that might differ between human and AI writing:**
Human writing compared to that of AI writing tends to be lumpier: smaller sentences, a narrower vocabulary, and the higher likeliness of typos in text.

**What it can't see:**
The model does not understand the meaning of the text. This means that things like punctuation, quotes, and splitting sentences can possibly change its score. 

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** 
When the two signals disagree, they should be averaged equally. A disagreement should produce a middle score and an "unsure" label.

**The numbers:**
Both signals range from 0-1. A lower score means its more likely to be human, and a higher score means its more likely to be AI. Averaging both the numbers helps balance both signals when choosing what to really label a submission. This will help it reach the "unsure" label when the two signals do disagree.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
A case where my two signals split is:
- "Why does everyone want to cut in line? What is their issue can't everyone just wait?"
The model signal returned 0.2886, which is in the human range. The style
signal returned 0.5685, which is in the unsure range. Because the signals
disagree, my rule averages them equally:
`(0.2886 + 0.5685) / 2 = 0.4286`
The combined score is in the unsure range, so the system avoids making a
confident label.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00-0.35 | "We think this was probably written by a person." |
| unsure | 0.35-0.65 | "We cannot confidently determine whether AI or a human wrote this." |
| high-confidence AI | 0.65-1.00 | "We think this was probably generated by AI." |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
I worded the "unsure" label this way because a disagreement between the two
signals can move the combined score into the uncertainty range. Instead of
making a confident guess that could be incorrect, the system tells the reader
that it cannot determine confidently whether AI or a human wrote the submission.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"text\":\"The rain started before breakfast. I forgot my umbrella and arrived at work with wet shoes. At least the coffee was still warm.\",\"creator_id\":\"demo_writer\"}"
```


```json
{
  "confidence": 0.3792,
  "content_id": "c_c77a5d177704",
  "creator_id": "demo_writer",
  "guess": "analyzed",
  "label": "model score calculated",
  "model_score": 0.3792,
  "style_score": null
}

```

**An appeal**

```bash
curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d "{\"content_id\":\"c_3447df8c7242\",\"reasoning\":\"I wrote this submission myself and request a review.\"}"
```

```json
{
  "content_id": "c_3447df8c7242",
  "message": "Appeal recorded for review.",
  "status": "under_review"
}

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
     "timestamp": "2026-10-29T20:03:06+00:00", 
     "content_id": "c_3447df8c7242", 
     "creator_id": "calibration_lightly_edited_ai", 
     "event": "appeal", 
     "status": "under_review", 
     "reasoning": "I wrote this submission myself and request a review."
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
I asked Copilot for more clarification on how the system needs to overall work. I was confused on the steps it takes on how the routing works from when a submission is sent to the feedback it needs to give.

- *What came back:*
Copilot explained how the routing worked, what was submitted, how to properly get into the server by opening app.py, and how to submit text. It also explained to me how everything was logged and formated into what was the audit log that holds every run.

- *What I changed:*
This helped me with fully explaining how the system should properly work in the "What this does" section.


**Moment 2**

- *What I asked for:*
I asked Copilot to explain how each threshold maps to each label and what gets measured.

- *What came back:*
Copilot explained that two signals are used, the model signal and style signal. The model signal measures perplexity, while the style signal measures 3 things: sentence length spread, the token ratio, and the punctuation density.

- *What I changed:*
This helped me understand what each model can't see and helped me with implementing the combining rule for cases when the two signals disagree.


<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I chose 5 submissions per minute because a real writer should have enough time to submit a few revisions without being blocked. I chose 50 submissions per day to allow regular daily use while limiting spam and automated attacks that try to repeatedly test the system.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

200 200 200 200 200 429 429 429 429 429 429 429 429 429 429

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
1. {"timestamp": "2026-11-05T02:07:13+00:00", "content_id": "c_ffa1417eb23e", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.3333, "combined_score": 0.16665, "label": "We think this was probably written by a person.", "status": "decided"}

2. {"timestamp": "2026-11-05T02:07:11+00:00", "content_id": "c_33af409a79b2", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6208, "combined_score": 0.71295, "label": "We think this was probably generated by AI.", "status": "decided"}

3. {"timestamp": "2026-11-05T02:07:12+00:00", "content_id": "c_a68b31f4e27b", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.5752, "combined_score": 0.7283, "label": "We think this was probably generated by AI.", "status": "decided"}

4. {"timestamp": "2026-11-05T02:07:13+00:00", "content_id": "c_70839f7075e0", "creator_id": "attacker_MF04", "guess": "human", "model_score": 0.0112, "style_score": 0.5, "combined_score": 0.2556, "label": "We think this was probably written by a person.", "status": "decided"}

5. {"timestamp": "2026-11-05T02:07:14+00:00", "content_id": "c_1f5b0d29d441", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.8343, "combined_score": 0.91095, "label": "We think this was probably generated by AI.", "status": "decided"}

6. {"timestamp": "2026-11-05T02:07:14+00:00", "content_id": "c_ebd3e977c737", "creator_id": {"id": "x"}, "guess": "human", "model_score": 0.0492, "style_score": 0.4815, "combined_score": 0.26535, "label": "We think this was probably written by a person.", "status": "decided"}

7. {"timestamp": "2026-11-05T02:07:13+00:00", "content_id": "c_092e6f262810", "creator_id": "attacker_PI06", "guess": "unsure", "model_score": 0.5583, "style_score": 0.5995, "combined_score": 0.5789, "label": "We cannot confidently determine whether AI or a human wrote this.", "status": "decided"}

8. {"timestamp": "2026-11-05T02:07:12+00:00", "content_id": "c_c505458cb145", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.6171, "combined_score": 0.74935, "label": "We think this was probably generated by AI.", "status": "decided"}

9. {"timestamp": "2026-11-05T02:07:13+00:00", "content_id": "c_62694fd8e7be", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 0.5, "combined_score": 0.7484500000000001, "label": "We think this was probably generated by AI.", "status": "decided"}

10. {"timestamp": "2026-11-05T02:07:14+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}


```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

The worst outcome was the false positive on FP03. This is the worst becasue the system shows that it accused a real writer on being AI due to careful,formal writing from a Non-Native English speaker. The error occured at the signal and label stages, which means the model produced a high model score, and the combining rule made it so the label resulted towards AI.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

- **Note:** Criterion 4 was tested manually outside `scenarios.py`. Three valid appeals returned `under_review`, and each appeal’s reasoning was recorded in the audit log.

- **Note:** To run all scenerios sucessfully, token limiting was turned OFF to properly evaluate and decide a verdict for all runs.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | 1/10 | 3/10  | 3/10  | 3/10 | MISS |
| 2. score spread | >=/.20 | .0193 | .0193  | .0193 | MISS |
| 3. label coverage | At least 1 AI, 1 Unsure, 1 human label | AI, Unsure | AI, Unsure |  AI, Unsure | MISS |
| 4. appeal path | Every appeal changes to under_review and has reasoning | 3/3 | 3/3 | 3/3 | PASS |
| 5. bad input | Missing, empty, or enormous text returns 400 | All 3 returned 400  | All 3 returned 400  | All 3 returned 400  | PASS |


**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Source: `results/run_2026-11-05_1141_before.md`
Function: `run_eval.py::main`
Trial: 1 — Criterion 1, my own writing


```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6003000000000001,
    "model_score": 0.5865,
    "style_score": 0.6141,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "Tuesday afternoon, I saw a homeless man on the train begging for chang"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.73725,
    "model_score": 0.8659,
    "style_score": 0.6086,
    "label": "We think this was probably generated by AI.",
    "sent": "Its 10 o'clock at night and I just got in my car. I am on my way to ge"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.55095,
    "model_score": 0.6868,
    "style_score": 0.4151,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "I am sitting at home, it is 9:39 PM and I am working on a project, but"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48145000000000004,
    "model_score": 0.3584,
    "style_score": 0.6045,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "The animals in my farm like to eat hay by the barn. The fields see the"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6342,
    "model_score": 0.7341,
    "style_score": 0.5343,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "The African Sahara is home to lions, jaguars, and cheetahs. The locals"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.63425,
    "model_score": 0.7788,
    "style_score": 0.4897,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "There is a man in the forest chopping down trees to build a cabin for "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5187999999999999,
    "model_score": 0.4839,
    "style_score": 0.5537,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "In the sea there is plenty of fishes, some of them even give wishes. T"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.673,
    "model_score": 0.7482,
    "style_score": 0.5978,
    "label": "We think this was probably generated by AI.",
    "sent": "I was at the park today, and there was a lot of families with their ch"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.63885,
    "model_score": 0.7234,
    "style_score": 0.5543,
    "label": "We cannot confidently determine whether AI or a human wrote this.",
    "sent": "There was a lot of cars in the highway, and they were all driving down"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6984999999999999,
    "model_score": 0.7272,
    "style_score": 0.6698,
    "label": "We think this was probably generated by AI.",
    "sent": "A group of dogs were digging through the trash behind a bar. A custome"
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

Criterion 1: MISS
Stage: Both Signals and the combining rule.
Mechanism: Three of the known to be human samples obtained a combined score of .65, so averaging the model and style scores pushed the score into the AI range.

Criterion 2: MISS
Stage: Both Signals and the combining rule.
Mechanism:The 10 human and 10 AI samples produced close score averages (which were .5947 for human and .6140 for the AI). The signals did not strongly distinguish the two labels to reach the .20 difference for the criterion.

Criteiron 3: MISS
Stage: Both signals and the combining rule.
Mechanism:None of the three runs scored below a .35, which is the 'human' label range. This meant that the 'human' label was unreachable. The system only produced 'ai' and unsure 'labels'.

All 3 misses have one pattern, they all fail at the signals and combining rule stages. It seems that most of the scoring was in the middle to higher range, which lead to overall 'unsure' and 'ai' labels throughout all runs. This made no room for the 'human' range to appear, which means an issue could be with the thresholds for each label.


---

## The Improvement

**What I changed:**
I widened the unsure threshold from to be up to .75. This means the AI threshold his now .75-1.

**Which diagnosis pointed at it:**
It pointed at the criterion 1 diagnosis which showed some human writing that was incorrectly labelled 'ai'. Raising the threshold gives human writing more of a chance of recieving the 'unsure' label instead of being confidently labelled 'ai'.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | 1/10 | 0/10  | 0/10 |  0/10 | PASS |
| 2. score spread | >=.20 | .0193  | .0193  | .0193 | MISS |
| 3. label coverage | At least 1 AI, 1 Unsure, 1 human label | Unsure only | Unsure only  | Unsure only | MISS |
| 4. appeal path | Every appeal changes to under_review and has reasoning | 3/3 | 3/3 | 3/3 | PASS |
| 5. bad input | Missing, empty, or enormous text returns 400 | All 3 returned 400  | All 3 returned 400  | All 3 returned 400  | PASS |


**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->
Widening the unsure threshold made it so the first criterion passes. No human writing was labelled as 'ai', which gave the human writing a chance at being labelled 'unsure' instead of having a higher score that falls into the 'ai' range.

However, the change did weaken Criterion 3. The AI sample scored below the new .75 threshold mark, so all 3 samples in all 3 runs recieved 'unsure'. This means the system reduced false psotiives, but lost access towards the 'ai' labels for the test inputs.


---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->
The scoring pipeline is still an issue. Criterion 3 still fails because the scoring for the human, borderline, and ai samples all fall in the 'unsure' range. Criterion 2 also still remains broken, since the average scores for known human and ai writing differ about .0193, which is far below the .20 goal. The signals do not help to clearly distinguish the human and ai writing enough.

Something I would do to try and fix these issues would be to improve the calibration of the model and style signals using known human and known ai samples. I would try to reweight these signals based on those results. Changing the style signal to be higher can help with identifying differences in sentence structure and grammar. 

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
