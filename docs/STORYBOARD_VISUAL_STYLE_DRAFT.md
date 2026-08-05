# Q-Forge Demo Video — Storyboard & Visual Style Discussion Draft

> Status: discussion draft  
> Project: Q-Forge  
> Submission: AMD Hackathon 2026, Track 3 — Physical AI  
> Author / Team: Cao Yuhao  
> Target runtime: approximately 4 minutes 39 seconds  
> Canvas: 1920 × 1080, 16:9, 24 FPS

## 1. Narrative objective

The video should follow one clear causal story:

```text
Physical AI problem
  → Q-Forge method
  → frozen paired protocol
  → same-state behavioral evidence
  → aggregate paired result
  → gains and regressions
  → AMD implementation and profiling
  → policy-level inference optimization
  → conclusion and submission identity
```

The video is not intended to reproduce every experiment in the repository. Its
job is to make the project understandable in the first minute, credible by the
third minute, and technically relevant to AMD by the final minute.

The four facts the audience should remember are:

1. Q-Forge improves a frozen SmolVLA policy at inference time using a learned Q critic.
2. Paired success improves from `21/50` to `34/50` reset states.
3. There are 19 failure-to-success transitions and 6 success-to-failure regressions; exact McNemar `p=0.0146`.
4. The system was built and profiled on AMD Radeon `gfx1100`, with policy latency reduced by approximately `10.1%` without retraining.

## 2. Overall visual language

### 2.1 Canvas and rendering

- Resolution: `1920 × 1080`.
- Aspect ratio: `16:9`.
- Frame rate: `24 FPS`.
- Final video codec: H.264, YUV420P.
- Audio: AAC.
- All layouts must reserve a subtitle-safe area at the bottom.
- Charts and footnotes should remain legible after normal video compression.

### 2.2 Color system

| Role | Color | Hex |
|---|---|---:|
| Background | Deep blue-black | `#09111F` |
| Primary panel | Dark slate | `#151E32` |
| Secondary panel | Dark blue | `#192741` |
| Panel outline | Muted blue | `#31405F` |
| Primary text | White | `#FFFFFF` |
| Secondary text | Gray-blue | `#9FB0CC` |
| Muted text | Steel blue | `#7F93B3` |
| Base policy / SDPA | Blue | `#57B8FF` |
| Q-guidance / success | Green | `#64D9AC` |
| FA-CK / failure / warning | Red | `#EF5B67` |
| Triton / trade-off | Orange | `#F2B45F` |

Color semantics must remain consistent across the full video:

- Blue always denotes the Base policy or the SDPA baseline.
- Green denotes Q-guidance, accepted improvements, or successful outcomes.
- Red denotes failures, regressions, or FA-CK when shown in backend charts.
- Orange denotes Triton or a performance/engineering trade-off.
- Gray denotes unchanged outcomes, supporting detail, or inactive paths.

### 2.3 Typography

- Preferred family: Inter.
- Portable fallback: DejaVu Sans / Arial / sans-serif.
- Main scene title: approximately `48–58 px`, semibold or bold.
- Panel title: approximately `26–32 px`, bold.
- Main numeric result: approximately `54–76 px`, bold.
- Body text: approximately `20–27 px`.
- Footnotes: approximately `15–18 px`.
- Avoid paragraphs longer than two short lines on screen.
- Avoid showing more than three levels of text hierarchy on one scene.

### 2.4 Shape language

- Rounded panels with approximately `20–28 px` corner radius.
- Thin `1–2 px` panel borders.
- Avoid glossy gradients, skeuomorphic controls, or heavy shadows.
- Use soft glows only for success/failure moments, not for every card.
- Data-flow arrows should be narrow, clean, and directional.
- Real robot footage should use subtle colored borders rather than decorative frames.

### 2.5 Motion language

Only three primary animation patterns should be used:

1. **Fade and rise** — titles and cards fade in while moving upward by approximately 10–20 px.
2. **Path drawing** — pipeline arrows and action trajectories draw from source to destination.
3. **Result emphasis** — key numbers scale from approximately 96% to 100% and receive a brief color pulse.

Recommended animation duration:

- Small text/card entrance: `300–450 ms`.
- Major panel transition: `450–650 ms`.
- Result pulse: `250–350 ms`.
- Avoid bouncing, rotating, or high-energy gaming-style effects.

### 2.6 Subtitle specification

- Transparent background.
- Exactly one line of subtitle text per cue.
- No newline within a cue.
- Cue boundaries follow speech progression and word timing.
- White text with a dark outline and light shadow.
- Bottom-centered placement.
- Video visuals must leave approximately 140–160 px of bottom-safe space.
- Do not place chart legends, axes, or essential footnotes behind subtitles.

## 3. Proposed timeline

The current video contains eight major chapters. The long second chapter should
contain three internal visual beats so that no static slide remains on screen for
approximately 80 seconds.

| Time | Scene | Primary purpose |
|---|---|---|
| `00:00–00:18` | 1. Title / Hook | Explain the project in one sentence |
| `00:18–00:42` | 2A. Physical AI problem | Show why a capable policy still fails |
| `00:42–01:10` | 2B. Why inference-time guidance | Explain why Q-Forge does not retrain the policy |
| `01:10–01:38` | 2C. Frozen evaluation protocol | Establish paired-evaluation credibility |
| `01:38–02:20` | 3. Q-Forge architecture | Explain the offline and inference pipelines |
| `02:20–02:57` | 4. Paired closed-loop case | Show Base failure vs Q-guidance success |
| `02:57–03:17` | 5. 50-state paired result | Present the main quantitative result |
| `03:17–03:34` | 6. Behavioral transitions | Show both improvements and regressions |
| `03:34–03:52` | 7A. AMD attention benchmark | Present forward/backward/full-step profiling |
| `03:52–04:10` | 7B. Policy inference optimization | Present policy-level latency improvement |
| `04:10–04:38.6` | 8. Conclusion / Submission | Close with three takeaways and identity |

## 4. Scene-by-scene storyboard

### Scene 1 — Title / Hook

**Time:** `00:00–00:18`

**Objective:** Answer three questions immediately: what the project is, what it
improves, and which hackathon track it belongs to.

**On-screen copy:**

```text
Q-FORGE
Value-Guided Action Refinement for Physical AI

Improving a frozen SmolVLA policy at inference time

AMD Hackathon 2026 · Track 3: Physical AI · Cao Yuhao
```

**Layout:**

- Left 58%: project title, subtitle, and submission identity.
- Right 42%: a real LIBERO stove/bowl/plate observation.
- Overlay two simplified action trajectories:
  - Base trajectory in blue, ending with a red failure mark.
  - Guided trajectory in green, reaching the target with a success mark.

**Animation:**

1. `Q-FORGE` fades in.
2. Subtitle appears.
3. Blue Base trajectory draws and stops at failure.
4. Green guided trajectory draws to the target.
5. Track and author identity fade in last.

**Avoid:** architecture diagrams, success-rate tables, unexplained abbreviations,
or long technical claims on the opening scene.

---

### Scene 2A — Physical AI problem

**Time:** `00:18–00:42`

**Title:**

```text
A capable policy can still choose the wrong action chunk
```

**Objective:** Show that the frozen policy already has useful capability, but a
single poor action-chunk decision can turn a solvable state into a failure.

**Layout:**

- Left: one real LIBERO observation.
- Right: four candidate action chunks radiating from the same observation.
- A critic score bar appears beside each candidate.
- The preferred candidate receives a green border and the others fade slightly.

Do not invent precise Q values unless they come from an audited sample. Relative
bars are sufficient:

```text
Candidate A  ██
Candidate B  ████
Candidate C  ████████  ← selected
Candidate D  ███
```

**Boundary statement:**

```text
The checkpoint is frozen. Only inference-time action selection changes.
```

---

### Scene 2B — Why inference-time guidance

**Time:** `00:42–01:10`

**Title:**

```text
Improve behavior without retraining the policy
```

**Objective:** Explain the design choice and distinguish Q-guidance from policy
retraining or unconstrained online RL.

**Layout:** three vertical cards.

| Card | Main text | Status |
|---|---|---|
| Retraining | Weight update · expensive | Not the focus |
| Q selection | Choose among candidates · conservative | Safe baseline |
| Q guidance | Refine the action chunk · gate-checked | Selected method |

The Q-guidance card should be highlighted in green.

**Gate visualization:**

```text
Validation-approved configuration
        ↓ pass
Enable Q guidance

        ↓ fail
Conservative diagnostics only
```

Preferred explanatory sentence:

```text
Only validation-approved guidance settings are used at evaluation time.
```

**Bottom boundary strip:**

```text
No policy retraining · No online environment gradients · Frozen checkpoint
```

---

### Scene 2C — Frozen paired evaluation protocol

**Time:** `01:10–01:38`

**Title:**

```text
A frozen, paired evaluation protocol
```

**Objective:** Establish the protocol before revealing the result, so the result
does not look like a cherry-picked pair of videos.

**Primary numeric cards:**

```text
50 reset states
1 fixed seed
240 max steps
5 actions per replan
```

**Paired diagram:**

```text
State 0  ─┬─ Base
          └─ Q-guidance

State 1  ─┬─ Base
          └─ Q-guidance

...

State 49 ─┬─ Base
          └─ Q-guidance
```

**Side checklist:**

```text
Same checkpoint
Same initial state
Same seed
Same task
```

**Protocol footnote:**

```text
Primary paired study: one LIBERO task, reset states 0–49, seed 2001.
```

This detail should be visible but should not become the headline of the entire project.

---

### Scene 3 — Q-Forge architecture

**Time:** `01:38–02:20`

**Title:**

```text
Q-Forge: value-guided refinement around a frozen VLA
```

**Objective:** Explain the system with one architecture diagram and separate the
offline critic-building path from the inference path.

**Diagram:**

```text
                            OFFLINE

Base-policy rollouts
        ↓
Perturbed action chunks
        ↓
Q-labeled transitions
        ↓
QVGM critic: state + action chunk → Q

                           INFERENCE

Observation + language
        ↓
Frozen SmolVLA
        ↓
Base action chunk a₀
        ↓
Q-guidance under bounded constraints
        ↓
Executable action chunk
```

**Constraint labels beside Q-guidance:**

```text
Bounded action delta
Limited optimization steps
Validation-approved configuration
```

**Animation sequence:**

1. Offline data path draws from rollout to critic.
2. Offline path dims.
3. Inference observation enters the frozen policy.
4. Base action chunk appears.
5. Critic evaluates `Q_base`.
6. A short green refinement path moves the action to `Q_guided`.
7. The constrained executable chunk exits the panel.

**Avoid:** full critic layer diagrams, complete loss equations, checkpoint paths,
or every training stage. Those belong in the README.

---

### Scene 4 — Paired closed-loop case

**Time:** `02:20–02:57`

**Title:**

```text
Same reset. Same seed. Different outcome.
```

**Objective:** Provide the most intuitive behavioral evidence.

**Layout:** synchronized side-by-side video.

```text
┌──────────────────────────┬──────────────────────────┐
│ BASE                     │ Q-GUIDANCE               │
│                          │                          │
│ Real LIBERO episode      │ Real LIBERO episode      │
│                          │                          │
│ FAILURE                  │ SUCCESS                  │
│ State 1 · Seed 2001      │ State 1 · Seed 2001      │
└──────────────────────────┴──────────────────────────┘
```

**Synchronization requirements:**

- Same reset state and seed.
- Both videos start together.
- Same playback speed.
- No speed ramp that favors one method.
- If one episode finishes early, hold its final frame and keep the outcome visible.

**Visual behavior:**

- Base begins with a blue frame; it becomes red when failure is determined.
- Q-guidance uses a green frame; the target receives one brief green pulse on success.
- Avoid covering the robot, bowl, plate, or gripper with large labels.

---

### Scene 5 — 50-state paired result

**Time:** `02:57–03:17`

**Title:**

```text
Q-guidance improves paired success across 50 reset states
```

**Primary result:**

```text
Base                 Q-guidance
21 / 50              34 / 50
42%                  68%

          +13 successes
          +26 percentage points
```

**Paired outcome summary:**

```text
Failure → Success    19
Success → Failure     6
Unchanged            25

Exact McNemar p = 0.0146
```

**Preferred chart:** a 50-cell paired reset-state matrix.

- Green: failure → success.
- Red: success → failure.
- Blue-green: success → success.
- Dark gray: failure → failure.

The matrix makes it clear that this is a paired comparison, not two unrelated percentages.

**Footnote:**

```text
LIBERO-Spatial task 7 · reset states 0–49 · seed 2001 · frozen protocol
```

---

### Scene 6 — Behavioral transitions

**Time:** `03:17–03:34`

**Title:**

```text
Paired transitions reveal both gains and regressions
```

**Objective:** Show the complete paired outcome rather than only the net success increase.

**Sankey structure:**

```text
BASE                              Q-GUIDANCE

Failure 29 ────── 10 ─────────▶ Failure
           ╲
            ╲──── 19 ─────────▶ Success

Success 21 ────── 15 ─────────▶ Success
           ╲
            ╲───── 6 ─────────▶ Failure
```

**Color:**

- Failure → Success: thick green flow.
- Success → Failure: thinner red flow.
- Success → Success: blue-green flow.
- Failure → Failure: dark gray flow.

**Conclusion:**

```text
Net gain: +13 successes
```

**Credibility statement:**

```text
Guidance helps substantially, but does not eliminate regressions.
```

---

### Scene 7A — AMD attention benchmark

**Time:** `03:34–03:52`

**Title:**

```text
Built and profiled on AMD Radeon
```

**Hardware strip:**

```text
gfx1100 · 96 CUs · 48 GiB VRAM · PyTorch 2.8 + ROCm 6.4
```

**Three charts on one page:**

1. Forward throughput — TFLOP/s, higher is better.
2. Backward throughput — TFLOP/s, higher is better.
3. FWD+BWD complete step — milliseconds, lower is better, log scale.

Each chart compares:

- CK FlashAttention in red.
- Triton FlashAttention in orange.
- PyTorch SDPA in blue.

**Microbenchmark label:**

```text
Kernel microbenchmark · B=8 · H=16 · D=64 · causal FP16
```

**Conclusion:**

```text
CK dominates long-sequence forward throughput.
SDPA remains faster for backward and complete training steps.
```

This page must not imply that long-sequence kernel speedup is equal to complete
SmolVLA policy speedup.

---

### Scene 7B — Policy inference optimization

**Time:** `03:52–04:10`

**Title:**

```text
10.1% lower policy latency without retraining
```

**Objective:** Present policy-level inference improvement separately from the
attention kernel benchmark.

**Main comparison:**

```text
Baseline
321.8 ms/replan  ████████████████████████████████

Optimized
289.3 ms/replan  █████████████████████████████

1.112× faster
−32.5 ms/replan
```

**Optimization chips:**

```text
Auto fused SDPA
Inference mode
Static denoising loop
Language/layer cache
Lightweight action output
Invariant denoising layout cache
```

**Latency protocol:**

```text
Fixed observation and explicit noise · GPU synchronized · 30 runs · median
```

**Numerical drift:**

```text
Maximum action difference: 9.3e−4
Mean action difference: 1.8e−4
```

**Optional tail-latency card:**

```text
P90
362.0 ms → 300.0 ms
```

**Do not show on this page:**

- Whole rollout or episode duration.
- LIBERO environment step time.
- The nearly tied `SDPA 314.2 ms` versus `FA-CK 313.4 ms` policy result.
- A direct claim that CK kernel TFLOP/s equals end-to-end policy speedup.

---

### Scene 8 — Conclusion / Submission

**Time:** `04:10–04:38.6`

**Title:**

```text
Q-Forge
A practical inference-time upgrade for Physical AI
```

**Three takeaway cards:**

```text
68% success
34 / 50 paired resets
```

```text
+13 net successes
Exact McNemar p = 0.0146
```

```text
10.1% lower policy latency
on AMD Radeon
```

**Closing sentence:**

```text
A frozen SmolVLA policy, improved through value-guided action refinement and AMD-aware inference.
```

**Submission identity:**

```text
Team: Cao Yuhao
Track 3: Physical AI
GitHub: ZorAttC
Project: Q-Forge
```

When the public repository is available, add a short link and QR code. Until then,
do not display a temporary or invalid URL. A placeholder may read:

```text
Repository prepared for public release
```

Hold the final visual for approximately 3–5 seconds. Do not cut directly to black
on the final spoken word.

## 5. Scene transitions

Default transition:

```text
Previous page scales to 98%
  + approximately 150 ms soft blur
  + next page fades in over 350–500 ms
```

Semantic transitions should connect related evidence:

- Architecture → paired video: the diagram splits into Base and Q-guidance halves.
- Paired video → result: outcome labels shrink into the 50-state matrix.
- Result matrix → Sankey: the 50 cells regroup into four transition flows.
- AMD kernel page → policy latency: the three kernel charts move left or dim while the policy-level latency bars expand.

Avoid unrelated wipe directions, 3D page turns, or random transitions between scenes.

## 6. Evidence and wording rules

### 6.1 Claims that are safe to show

- Frozen SmolVLA checkpoint.
- Inference-time Q-guidance.
- Base `21/50`; Q-guidance `34/50`.
- 19 failure-to-success; 6 success-to-failure.
- Exact McNemar `p=0.014633298`, rounded visually to `0.0146`.
- AMD Radeon `gfx1100`, 96 CUs, 48 GiB VRAM.
- CK forward kernel throughput advantage in the measured long-sequence sweep.
- SDPA backward/full-step advantage in the measured training benchmark.
- Policy latency approximately `321.8 → 289.3 ms/replan` under the fixed-input synchronized protocol.
- Approximately `10.1%` lower policy latency without retraining.

### 6.2 Claims that require careful wording

- Do not describe the primary result as a broad multi-task benchmark.
- Do not imply that a single paired example proves aggregate success.
- Do not equate attention TFLOP/s with complete policy speedup.
- Do not present a whole-episode rollout time as policy inference latency.
- Do not describe Q-guidance as PPO or online RL.
- Do not claim regressions were eliminated.
- Do not claim that FA-CK materially improves current batch-1 SmolVLA policy latency.

### 6.3 Preferred terminology

Use:

```text
validation-approved guidance settings
paired reset-state evaluation
frozen policy checkpoint
bounded action refinement
policy-only synchronized latency
failure-to-success transition
```

Avoid unexplained shorthand such as:

```text
gate-selected config
validation disagreement
single-seed SOTA
rollout speedup
```

unless each term has already been defined on screen.

## 7. Video content versus documentation content

### 7.1 Keep in the video

- Project identity and one-sentence value proposition.
- Frozen policy and inference-time refinement.
- Q-guidance architecture and bounded constraints.
- Paired episode evidence.
- `21/50 → 34/50`.
- 19 improvements and 6 regressions.
- Exact McNemar `p=0.0146`.
- AMD kernel benchmark summary.
- Policy latency `321.8 → 289.3 ms`.
- Author, Track, and GitHub identity.

### 7.2 Keep primarily in README / submission documentation

- Full critic architecture.
- Cal-QL or MC critic loss details.
- Checkpoint and dataset paths.
- Complete Q-guidance hyperparameters.
- Full gate thresholds.
- 300-rollout collection details.
- Every random seed and configuration file.
- Full attention benchmark JSON.
- FA-CK block-prefix implementation details.
- Every inference optimization environment variable.
- Git commit hashes and rollback commands.
- Full limitations and failure analysis.

## 8. Asset checklist

### Existing or expected assets

- Q-Forge title graphic.
- Real LIBERO observation image.
- Paired Base and Q-guidance episode videos.
- 50-state paired result data.
- Behavioral transition counts.
- AMD attention benchmark JSON and SVG reports.
- Policy-latency benchmark JSON.
- Project name, author, Team, Track, and GitHub account.

### Assets still requiring a final decision

- Final public GitHub URL.
- QR code, after repository publication.
- Exact paired example frames and crop region.
- Whether the architecture scene uses a fully animated flow or progressive card reveal.
- Whether P90 appears on the policy-latency page or remains in documentation only.

## 9. Review checklist

Before the final render, verify:

- [ ] All charts state whether higher or lower is better.
- [ ] Kernel and policy-level results are visually separated.
- [ ] Every experimental number matches an auditable JSON/report.
- [ ] The paired video uses the same state, seed, and playback speed.
- [ ] Subtitle cues remain single-line with transparent background.
- [ ] Essential content remains above the subtitle-safe region.
- [ ] No on-screen text references a nonexistent public URL.
- [ ] The 50-state protocol footnote is visible.
- [ ] Regressions (`6`) are shown, not hidden.
- [ ] `p=0.0146` is described as an exact paired McNemar result.
- [ ] Policy latency is measured around `predict_action_batch()` only.
- [ ] The final page remains visible long enough to read.
- [ ] The final MP4 fully decodes and retains H.264/AAC compatibility.

## 10. Current recommended direction

The recommended final version uses 11 visual beats within the existing eight
chapter time windows. The most important structural change is to split the long
problem/method introduction into three visual beats and split the AMD chapter into:

1. a kernel-level profiling page; and
2. a separate policy-level latency page.

This keeps three different measurements conceptually separate:

```text
Attention kernel throughput
≠ complete policy inference latency
≠ whole-environment rollout duration
```

The resulting story balances method novelty, paired behavioral evidence,
statistical evidence, AMD engineering contribution, and honest limitations.
