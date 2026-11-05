# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 13:21
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_691b24ae5e10` | unsure | 0.386 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_bc25628ff9dc` | unsure | 0.543 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_2ad82f861199` | unsure | 0.599 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_424fda21e376` | unsure | 0.605 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_70d17bcec4c9` | unsure | 0.415 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_c1c4bebf01fb` | unsure | 0.550 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_9de19a631b92` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c_984714dd90b4` | unsure | 0.368 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_bdd836a37a5e` | unsure | 0.619 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_114ec9cc2664` | ai | 0.880 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_6cf1980abbd6` | unsure | 0.606 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c_8507a0e18efc` | unsure | 0.691 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_29b43805a3f6` | unsure | 0.713 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_b2787fa6f1b7` | unsure | 0.703 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_53734e20f0a2` | unsure | 0.728 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_c289891983e6` | unsure | 0.728 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_4f58efde4444` | unsure | 0.749 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c_d34af997cf84` | human | 0.305 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_00d7a8bf69b7` | unsure | 0.483 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_758657b72cd7` | human | 0.325 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_4c15dc604326` | unsure | 0.572 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_6e9fc57af0fd` | unsure | 0.456 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_39ff9b56daaa` | unsure | 0.449 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_1f82318b284e` | unsure | 0.579 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_8ab5cd45000a` | human | 0.167 |  |
| MF04 | malformed | text is only punctuation | 200 | `c_7fcbb594c792` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `c_f4da68a06a7b` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `c_c3f6826ce1fb` | unsure | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c_70f2a91958d2` | unsure | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c_40917e2f8af3` | unsure | 0.423 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `c_85b55246e216` | human | 0.265 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4095c0fb72bb` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_b3d92459218d` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_9f07858c4bc2` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4ec7b1256b66` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_c85e9819619c` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_691b24ae5e10",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.38565,
  "model_score": 0.1635,
  "style_score": 0.6078,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_bc25628ff9dc",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.54325,
  "model_score": 0.5943,
  "style_score": 0.4922,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_2ad82f861199",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.59895,
  "model_score": 0.6662,
  "style_score": 0.5317,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_424fda21e376",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6052500000000001,
  "model_score": 0.6114,
  "style_score": 0.5991,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_70d17bcec4c9",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.41464999999999996,
  "model_score": 0.3212,
  "style_score": 0.5081,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_c1c4bebf01fb",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5501,
  "model_score": 0.5727,
  "style_score": 0.5275,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_9de19a631b92",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6130500000000001,
  "model_score": 0.5862,
  "style_score": 0.6399,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_984714dd90b4",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3679,
  "model_score": 0.2452,
  "style_score": 0.4906,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_bdd836a37a5e",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6185,
  "model_score": 0.7042,
  "style_score": 0.5328,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_114ec9cc2664",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8798999999999999,
  "model_score": 0.9792,
  "style_score": 0.7806,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_6cf1980abbd6",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.60645,
  "model_score": 0.6175,
  "style_score": 0.5954,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_8507a0e18efc",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6907000000000001,
  "model_score": 0.7387,
  "style_score": 0.6427,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_29b43805a3f6",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.71295,
  "model_score": 0.8051,
  "style_score": 0.6208,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_b2787fa6f1b7",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.70305,
  "model_score": 0.8329,
  "style_score": 0.5732,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_53734e20f0a2",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7283,
  "model_score": 0.8005,
  "style_score": 0.6561,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_c289891983e6",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7283,
  "model_score": 0.8814,
  "style_score": 0.5752,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_4f58efde4444",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.74935,
  "model_score": 0.8816,
  "style_score": 0.6171,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_d34af997cf84",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.30525,
  "model_score": 0.3223,
  "style_score": 0.2882,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_00d7a8bf69b7",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.48325,
  "model_score": 0.4625,
  "style_score": 0.504,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_758657b72cd7",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3254,
  "model_score": 0.2044,
  "style_score": 0.4464,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_4c15dc604326",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5721,
  "model_score": 0.5943,
  "style_score": 0.5499,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_6e9fc57af0fd",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.45575,
  "model_score": 0.4998,
  "style_score": 0.4117,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_39ff9b56daaa",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.44905,
  "model_score": 0.6401,
  "style_score": 0.258,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_1f82318b284e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5789,
  "model_score": 0.5583,
  "style_score": 0.5995,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_8ab5cd45000a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.16665,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_7fcbb594c792",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_f4da68a06a7b",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.83215,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_c3f6826ce1fb",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.7484500000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_70f2a91958d2",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_40917e2f8af3",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.42279999999999995,
  "model_score": 0.2395,
  "style_score": 0.6061,
  "label": "We cannot confidently determine whether AI or a human wrote this.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_85b55246e216",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.26535,
  "model_score": 0.0492,
  "style_score": 0.4815,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_4095c0fb72bb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.31739999999999996,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_b3d92459218d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.31739999999999996,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_9f07858c4bc2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.31739999999999996,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_4ec7b1256b66",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.31739999999999996,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_c85e9819619c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.31739999999999996,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
