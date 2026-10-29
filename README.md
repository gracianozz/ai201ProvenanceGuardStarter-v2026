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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



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
