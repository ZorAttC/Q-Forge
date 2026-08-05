# Q-Forge 演示视频 Storyboard 核心摘要 V2

> 版本定位：按照 Q-VGM 的问题动机组织项目开头。  
> 核心贡献：在 SmolVLA 上系统探索三种基于 Q-learning 的策略提升方式，并通过
> Task 7 主实验与 Task 3 diagnostic replication 表明 Q-guidance 都是当前最强的
> 路线；它无需重新训练 policy，而 residual 路线提供部署时免 critic 的选择。  
> 视频总时长：约 4 分 15 秒。  
> 页面数量：15 张。

## 录制前置原则：先冻结逐页文案，再生成任何视频资产

本版本采用严格的“一页一稿”生产流程。幻灯片、配音、字幕、时间对齐和最终视频
都必须以同一份 15 段文字稿为唯一来源，不再允许首页与下一页共用一段旁白，也不
允许先画页面、再临时补口播。

```text
确认项目事实与数字
→ 冻结 15 页屏幕文案
→ 冻结 15 段完整英文口播
→ 生成配音与字符级时间戳
→ 按段落边界生成 15 页幻灯片
→ 生成单行字幕
→ 合成并逐页检查
```

**生产 gate：**

- 每一页必须有且只有一段完整口播。
- 口播顺序必须与第 1–15 页严格一致。
- 屏幕文字负责“让人一眼读懂”，口播负责解释因果，不逐字朗读页面。
- 任何实验数字变更时，必须同时更新本文件与 `video/narration.txt`。
- 修改 `video/narration.txt` 后，必须重新生成配音和 alignment，禁止复用旧时间戳。
- 正式构建必须同时通过文案、配音文件和 alignment 的哈希校验。
- 在 15 页文字稿未冻结前，不生成正式配音、字幕、录屏幻灯片或最终视频。

## 一句话项目定义

```text
Q-Forge explores how a learned action-value critic can improve a flow-matching
SmolVLA policy through selection, test-time guidance, or offline distillation.
```

中文表述：

```text
Q-Forge 探索如何利用从策略自身成败 rollout 中学习的 Q critic，
通过动作选择、测试时引导和离线蒸馏三条路线提升 flow-matching SmolVLA。
```

## 正式评分标准（100 分）

| 评分项 | 分值 | 最强证据 |
|---|---:|---|
| Robot capability performance | 30 | 幻灯片 8–11：Task 7 主实验与 Task 3 方法排序复现 |
| AMD Radeon GPU and ROCm adoption | 20 | 幻灯片 12–13：Radeon PRO W7000 Series profiling 与 `10.1%` 延迟优化 |
| Innovation and originality | 20 | 幻灯片 3–7：critic、perturb 数据和三种 value-learning 路线 |
| Real-world application value | 20 | 幻灯片 1–4、9：利用策略自身失败经验，无需新增专家标注 |
| Contributions to upstream open-source projects | 10 | 幻灯片 12–13：LeRobot ROCm backend、mask 兼容与 benchmark |

评分映射集中放在倒数第二张幻灯片，不在每页重复展示。

## 整体故事线

```text
Flow-matching VLA 很强，但 SFT 只能利用专家数据
→ 部署时产生的大量失败 rollout 没有被利用
→ 传统 on-policy RL 对真实机器人太贵，flow policy 又没有简单 likelihood
→ 因此训练一个离线 action-value critic
→ 探索三种把 Q 知识转化为策略能力的方式
→ selection 只“挑动作”
→ guidance 直接“改动作”
→ residual 把改进“写进 velocity field”
→ 四路配对实验表明 guidance 最强，residual 最适合免 critic 部署
→ 第二个 LIBERO 任务复现相同方法排序，并明确 diagnostic 边界
→ 在 AMD Radeon 上完成全流程、profiling 和推理优化
```

## 第二轮节奏优化

```text
00:00–00:45  Hook + problem：先给结果，再解释为什么需要 value learning
00:45–01:39  System + critic + data：只保留理解三种路线所需的技术细节
01:39–02:13  Three methods + frozen protocol：建立公平比较前提
02:13–02:53  Behavioral case + primary result：先看行为，再看统计
02:53–03:13  Cross-task replication：增强证据，同时明确 diagnostic 限定
03:13–03:49  AMD profiling + policy latency：从 kernel 落到端到端收益
03:49–04:15  Judging map + conclusion：不再引入新实验
```

节奏原则：

- 第 1 分钟只回答“问题是什么、为什么不是常规 RL、系统放在哪里”。
- 第 2 分钟结束前讲完 critic、数据和三条路线，不在结果后回补方法细节。
- 主结果必须在 3 分 18 秒前完整出现。
- Task 3 只作为第二任务 diagnostic replication，不伪装成第二个 primary result。
- AMD 部分同时给出 kernel 选择依据和最终 policy latency，避免只展示 microbenchmark。

## 逐页完整文案文字稿（正式录制源）

以下内容先于视觉制作冻结。每页的“屏幕定稿”规定观众必须看到的文字层级；“完整
英文口播”是正式配音源，并与 `video/narration.txt` 的 15 个自然段逐段对应。

### 第 1 页：标题与结果钩子

**屏幕定稿：**

```text
Q-FORGE
Learning from a VLA Policy's Own Experience

Three Q-learning paths for flow-matching SmolVLA

42% → 68%
Q-guidance · paired closed-loop · no policy retraining

AMD Hackathon 2026 · Track 3: Physical AI
Cao Yuhao · Q-Forge
```

**完整英文口播：**

```text
Q-Forge asks whether a flow-matching VLA can learn from its own experience. We
compare 3 Q-learning paths for SmolVLA. Q guidance raises paired success from
42% to 68% without retraining the policy.
```

**转场目的：** 先给出问题、研究范围和最强结果，再回到“为什么部署经验没有被
利用”。

### 第 2 页：VLA 能力与未利用的部署经验

**屏幕定稿：**

```text
VLA policies learn from demonstrations—
but deployment produces experience

Expert demonstrations → SFT → Base SmolVLA
                                  ↓
                      success + failure rollouts
                                  ↓
                       unused by imitation

Task success and failure become supervision.
```

**完整英文口播：**

```text
SmolVLA turns vision, language, and robot state into action chunks. Supervised
fine-tuning learns only from demonstrations, but deployment also produces
successes, failures, and near misses. Q-Forge treats those outcomes as
supervision.
```

**转场目的：** 从“有经验但不用”自然引出为什么不直接采用常规 on-policy RL。

### 第 3 页：为什么选择 off-policy value learning

**屏幕定稿：**

```text
Why off-policy value learning?

ON-POLICY POLICY GRADIENT
Fresh rollouts
Expensive interaction
Approximate denoising likelihood

OFF-POLICY VALUE LEARNING
Reuse replay
Learn from outcomes
No explicit likelihood
Action direction ∇A Q(s,A)

Learn value from replay. Use value to improve the flow policy.
```

**完整英文口播：**

```text
On-policy reinforcement learning needs fresh interaction and is awkward for
denoising policies without explicit action likelihoods. Q-Forge instead learns
a Q critic from replay. Its value ranks action chunks, and its gradient shows
how an action should change.
```

**转场目的：** 明确 value learning 的优势后，展示 critic 放在 SmolVLA 的哪个
位置。

### 第 4 页：端到端架构

**屏幕定稿：**

```text
From multimodal observation to value-improved action

RGB + language + proprioception
→ Frozen SmolVLM prefix
→ Flow-matching Action Expert
→ iterative velocity prediction
→ clean 5 × 7 action chunk
→ execute 5 actions and replan

20 demos → SFT Base → closed-loop replay → Q critic
                                            ↓
                         Selection · Guidance · Residual

Frozen flow policy, surrounded by an experience-and-value loop.
```

**完整英文口播：**

```text
A frozen SmolVLM prefix encodes vision, language, and robot state. The Action
Expert denoises a 5-by-7 chunk, executes 5 actions, then replans. Q-Forge adds
replay, 1 offline critic, and 3 ways to improve the Base policy.
```

**转场目的：** 先建立系统全貌，再放大 critic 的输入、ensemble 和训练 gate。

### 第 5 页：Q critic 与 validation gate

**屏幕定稿：**

```text
An action-sensitive Q ensemble

512D compact state
8D proprioception
5 × 7 executable action chunk
        ↓
5 independent Q networks

MC ranking → H-step TD → Cal-QL → validation gate

GATE
TD < 0.01 · success > failure · dataset > random
finite non-zero action gradient
```

**完整英文口播：**

```text
5 Q networks evaluate compact state features, proprioception, and executable
action chunks. Monte Carlo learning ranks outcomes, temporal-difference
learning refines local value, and Cal-QL limits unsupported actions. A held-out
gate checks ranking, conservatism, and usable gradients.
```

**转场目的：** 回答 critic 如何可信之后，再说明局部动作差异从哪里来。

### 第 6 页：闭环 perturb 与 chunk 数据

**屏幕定稿：**

```text
Turn closed-loop experience into local value supervision

50 reset states × 6 rollouts = 300 episodes

Perturb continuous arm controls
Preserve gripper semantics
Execute during closed-loop simulation

300 episodes
60,505 transitions
36 mixed-outcome reset states
Sliding action chunk H = 5

Perturbation creates nearby action-outcome supervision.
```

**完整英文口播：**

```text
We run 6 perturbed rollouts from each of 50 reset states. Perturbations affect
arm controls, not the gripper, and execute inside the simulator loop. This
produces 300 episodes and 60,505 transitions, including 36 states with both
success and failure.
```

**转场目的：** 数据建立后，集中解释同一个 critic 如何产生三条不同策略路线。

### 第 7 页：三种 Q-learning 路线

**屏幕定稿：**

```text
Three Q-learning strategies for SmolVLA

Q SELECTION · CHOOSE
Sample N=4 · score · choose
Weights frozen · critic online

Q GUIDANCE · EDIT
Bounded projected Q-gradient edit
Weights frozen · critic online

QVGM RESIDUAL · WRITE
Distill improvement into the velocity field
Offline fine-tune · no deployment critic

Selection chooses. Guidance edits. Residual writes.
```

**完整英文口播：**

```text
The same critic supports 3 routes. Selection samples and chooses. Guidance
makes a bounded Q-gradient edit without changing policy weights. Residual
distillation trains that improvement into the flow field, so deployment no
longer needs the critic.
```

**转场目的：** 方法讲完后立即冻结评测条件，避免结果被理解为不同设置间的横向
比较。

### 第 8 页：四路配对评测协议

**屏幕定稿：**

```text
One protocol, four policy-improvement paths

Base · Selection N=4 · Q Guidance · QVGM Residual

FROZEN PAIRED CONDITIONS
50 reset states
Seed 2001
240 max steps
5 actions per replan
Same task and Base checkpoint

Paired transitions + exact McNemar test
```

**完整英文口播：**

```text
All methods use the same reset states, seed, checkpoint, step limit, and
replanning schedule. This paired protocol reveals both improvements and
regressions and supports an exact McNemar test.
```

**转场目的：** 先建立可信度，再用同状态闭环仿真录像展示“动作变了、结果也
变了”。

### 第 9 页：同状态闭环案例

**屏幕定稿：**

```text
Same reset. Same seed. Different outcome.

BASE · FAILURE
Q GUIDANCE · SUCCESS

LIBERO-Spatial Task 7
Reset state 1 · Seed 2001 · Same checkpoint

Q-guidance changes the action—not the policy weights.
```

**完整英文口播：**

```text
In this recorded Task 7 comparison, both policies start from the same reset
and seed. The Base policy times out. Q guidance makes small action corrections
and completes the placement. Only the action changes, not the policy weights.
```

**转场目的：** 个案只负责建立直觉，下一页立即给出完整 50-state 统计结果。

### 第 10 页：四路核心结果

**屏幕定稿：**

```text
Action-direction improvement outperforms candidate selection

Base                 21 / 50 · 42%
Selection N=4        18 / 50 · 36%
Q Guidance           34 / 50 · 68%
QVGM Residual        32 / 50 · 64%

Q Guidance
19 improvements · 6 regressions
+13 net states · +26 percentage points · exact p = 0.0146

Residual
11 improvements · 0 regressions · exact p = 0.00098
```

**完整英文口播：**

```text
Across 50 states, Base succeeds 21 times. Selection reaches 18, residual 32,
and guidance 34. Guidance converts 19 failures to successes and causes 6
regressions: a net gain of 13 states, or 26 percentage points, with exact
p-value 0.0146.
```

**转场目的：** 结果页回答“谁最好”，下一页回答“相同方法排序是否只出现在一个
任务”。

### 第 11 页：第二任务复现实验

**屏幕定稿：**

```text
Same method ranking on a second LIBERO task

TASK 7 · PRIMARY
Base 42% · Selection 36% · Guidance 68% · Residual 64%

TASK 3 · DIAGNOSTIC REPLICATION
Base 76% · Selection 70% · Guidance 88% · Residual 86%

Task 3 guidance
6 improvements · 0 regressions · exact p = 0.03125

Conservative preset used:
held-out TD loss 0.0121 > 0.01 gate
```

**完整英文口播：**

```text
We repeat the pipeline on Task 3, where Base already scores 76%. Selection
reaches 70%, residual 86%, and conservative guidance 88%, with 6 improvements
and no regressions. Because the critic slightly misses the TD gate, we report
this as diagnostic replication.
```

**转场目的：** 完成机器人能力证据后，进入 AMD 平台实现与 profiling。

### 第 12 页：AMD Radeon 与 attention profiling

**屏幕定稿：**

```text
Built and profiled on AMD Radeon PRO

Radeon PRO W7000 Series · 48 GiB VRAM
gfx1100 architecture · 96 CUs
PyTorch 2.8.0+rocm6.4 · ROCm runtime 7.2.4

FORWARD · CK up to 5.25×
BACKWARD · SDPA faster
FULL STEP · SDPA faster

Choose the backend for the workload—not the headline.

Kernel microbenchmark · B=8 · H=16 · D=64 · causal FP16
```

**完整英文口播：**

```text
The workflow runs on an AMD Radeon Pro W7000 Series GPU with PyTorch
and ROCm. Composable Kernel is best for long-sequence forward passes, while
SDPA is faster for backward and full training steps. Backend choice follows
the workload.
```

**转场目的：** kernel 级选择之后，展示最终用户真正感知的 policy replan 延迟。

### 第 13 页：策略推理优化

**屏幕定稿：**

```text
10.1% lower policy latency without retraining

Baseline
321.8 ms / replan

Optimized
289.3 ms / replan

−10.1% · 1.112× speedup

Fused SDPA · inference mode · fixed denoising loop
language-token and layer-reference caches · lightweight output

Maximum action difference: 9.3e−4
Mean action difference: 1.8e−4

Upstream-ready LeRobot extensions
```

**完整英文口播：**

```text
At policy level, fused SDPA, inference mode, a fixed denoising loop, caches, and
lightweight output reduce replan latency by 10.1% without retraining. The
optimized policy remains numerically close to the baseline.
```

**转场目的：** 将技术结果映射到正式评分项，帮助评委快速核对证据。

### 第 14 页：评分证据映射

**屏幕定稿：**

```text
JUDGING CRITERIA · 100-POINT EVIDENCE MAP

30 ROBOT · T7 42% → 68% · T3 76% → 88% diagnostic
20 AMD · W7000 Series / ROCm · profiling · −10.1% latency
20 INNOVATION · Choose / Edit / Distill
20 APPLICATION · Reuse failures · no new demonstrations
10 OPEN SOURCE · LeRobot patches / benchmarks
```

**完整英文口播：**

```text
The evidence maps directly to all 5 judging categories: robot capability,
AMD and ROCm adoption, innovation, application value, and upstream-ready
open-source engineering.
```

**转场目的：** 最后一页只保留三个可记忆结论和提交身份，不再引入新信息。

### 第 15 页：结论与提交身份

**屏幕定稿：**

```text
Q-FORGE
Value learning for flow-matching Physical AI

THREE PATHS
Selection · Guidance · Residual
Guidance best · Residual critic-free

BEST NO-RETRAINING RESULT
Q Guidance · 34 / 50 · 68% · p = 0.0146

AMD-AWARE DEPLOYMENT
10.1% lower policy latency

Q-Forge · Cao Yuhao · Track 3: Physical AI
GitHub: ZorAttC
```

**完整英文口播：**

```text
Q-Forge learns from a policy's own experience. Guidance is the strongest
no-retraining path, residual enables critic-free deployment, and AMD
optimization lowers latency. Built by Cao Yuhao for AMD Hackathon Track 3.
```

**收尾原则：** 画面至少保留 1.5 秒无新增信息的尾帧，确保项目名、作者和 GitHub
身份可读。

---

## 幻灯片 1：项目标题

**时间：** `00:00–00:13`

**标题：**

```text
Q-Forge
Learning from a VLA Policy's Own Experience
```

**副标题：**

```text
Three Q-learning paths for flow-matching SmolVLA
```

**主要内容：**

- 使用录制的 LIBERO 闭环仿真场景作为背景，避免暗示真实机器人实验。
- 蓝色表示 Base SmolVLA，绿色表示 Q-guided action。
- 用一条失败轨迹和一条成功轨迹建立视觉冲突。

**底部信息：**

```text
AMD Hackathon 2026 · Track 3: Physical AI
Cao Yuhao · Q-Forge
```

---

## 幻灯片 2：VLA 的能力与 SFT 局限

**时间：** `00:13–00:28`

**标题：**

```text
VLA policies learn from demonstrations—but deployment produces experience
```

**主要内容：**

- Vision-Language-Action 模型连接多模态理解与连续机器人控制。
- SmolVLA 的 flow-matching Action Expert 通过多步 denoising 生成 action chunk。
- SFT 只能学习专家 demonstrations 中出现的行为。
- 策略部署后会产生大量成功、失败和次优 rollout，但 imitation loss 不会利用这些经验。

**核心画面：**

```text
Expert demonstrations ──▶ SFT ──▶ Base SmolVLA
                                      │
                                      ▼
                          successful + failed rollouts
                                      │
                              unused by imitation
```

**核心句：**

```text
The policy generates its own supervision signal through task success and failure.
```

---

## 幻灯片 3：为什么选择 off-policy value learning

**时间：** `00:28–00:45`

**标题：**

```text
Why not conventional policy-gradient RL?
```

**主要内容：**

- PPO/GRPO 等 on-policy 方法需要不断从当前策略采集新 rollout。
- 在真实机器人上，新数据昂贵且历史经验不能被充分复用。
- Flow-matching policy 通过迭代 denoising 生成动作，没有简单的显式 action likelihood。
- Q critic 可以利用 replay data，同时从成功和失败经验中学习。
- Q-gradient 还能提供“动作应该向哪个方向变化”的一阶信息。

**对比画面：**

| On-policy policy gradient | Off-policy value learning |
|---|---|
| 每轮需要新 rollout | 可以复用历史 rollout |
| 依赖 likelihood/近似 likelihood | 不需要显式 action likelihood |
| 标量 advantage | 动作方向梯度 `∇A Q(s,A)` |

**核心句：**

```text
Learn value from replay, then decide how that value should improve the flow policy.
```

---

## 幻灯片 4：整体架构与端到端 Pipeline

**时间：** `00:45–01:03`

**标题：**

```text
Q-Forge architecture: from multimodal observation to value-improved action
```

**页面目的：** 先让评委看懂 SmolVLA 本身如何产生动作，再说明 Q-Forge 在什么
位置采集经验、训练 critic 和改善策略。

**SmolVLA 推理主干：**

```text
RGB observations + language instruction + proprioception
                         ↓
           SmolVLM visual-language prefix
                         ↓
          compact multimodal state representation
                         ↓
      Flow-matching Action Expert + initial noise x₁
                         ↓
        iterative velocity prediction vθ(xₜ, t)
                         ↓
             denoised action chunk x₀
                         ↓
             execute first 5 × 7 actions
```

**Q-Forge 外围闭环：**

```text
Few-shot demonstrations
        ↓
SFT Base SmolVLA
        ↓
closed-loop execution ──→ success / failure rollouts
        ↓                         ↓
Base action chunks          offline Q critic
        └──────────────┬──────────┘
                       ↓
       Selection · Guidance · Residual distillation
```

**视觉建议：**

- 中央画 SmolVLA 垂直主干，表明视觉、语言、状态如何进入 flow Action Expert。
- 左侧画 demonstrations → SFT → Base。
- 右侧画 rollout replay → critic。
- 底部将 critic 分叉到三种策略，但暂时只显示名称，不在本页解释细节。
- 冻结模块使用灰蓝色，训练/优化模块使用绿色或紫色。

**必须讲清楚：**

- SmolVLA 是 flow-matching policy，不是一次前向直接输出单步动作。
- Policy 生成完整 action chunk，但环境每次只执行前 5 个 7D 动作后重新规划。
- Q-Forge 的 critic 评估可执行 clean action chunk，而不是语言 token 或单个标量动作。

**核心句：**

```text
Q-Forge surrounds a frozen flow-matching VLA with an experience-and-value loop.
```

---

## 幻灯片 5：Q Critic 架构与学习原理

**时间：** `01:03–01:22`

**标题：**

```text
An action-sensitive Q ensemble for long-horizon manipulation
```

**Critic 输入：**

```text
Frozen SmolVLA prefix
→ fixed 512D compact feature zₛ

Robot proprioception
→ 8D state pₛ

Executable action chunk
→ 5 × 7 actions
```

**Critic 架构：**

```text
512D prefix feature ─┐
8D proprioception ──┼→ state encoder ─┐
                    │                 ├→ Q₁(s,A)
5×7 action chunk ───┘→ action input ──┼→ Q₂(s,A)
                                      ├→ ...
                                      └→ Q₅(s,A)
```

- 五个独立初始化的 Q network 组成 ensemble。
- `ensemble mean` 可用于 Q selection 的候选评分。
- `conservative min` 可用于保守 Q-guidance。
- `ensemble disagreement` 用于不确定性诊断和 gate。

**三阶段学习：**

```text
1. Monte-Carlo return regression · 5,000 steps
   学会成功轨迹应高于失败轨迹

2. H-step TD learning · 2,000 steps
   学习局部 chunk reward + 下一状态价值

3. Cal-QL conservative calibration
   压低 random / out-of-distribution actions 的虚高 Q
```

**核心公式只保留一个：**

```math
Q(z_s,p_s,A_{t:t+H-1})
\approx \mathbb E\left[\sum_k \gamma^k r_{t+k}\right]
```

**Validation gate：**

```text
held-out TD loss < 0.01
Q(success) > Q(failure)
Q(dataset) > Q(random)
action gradient finite and non-zero
```

**核心句：**

```text
The critic must rank outcomes, remain conservative off-distribution,
and provide usable action gradients.
```

---

## 幻灯片 6：Rollout、Perturb 增强与 Action Chunk 数据

**时间：** `01:22–01:39`

**标题：**

```text
Turn closed-loop experience into local action-value supervision
```

**Rollout 采集：**

```text
50 fixed reset states
× 6 rollouts per state
= 300 closed-loop episodes
```

**Perturb 增强：**

每个 state 使用六档局部动作扰动：

```text
{0.00, 0.01, 0.03, 0.03, 0.05, 0.05}
```

- 只对连续机械臂动作维度添加局部噪声。
- Gripper 维度不扰动，避免改变离散夹爪语义。
- Perturb 在闭环仿真执行中生效，因此会产生新的后续 observation 和任务结果。
- 它不是图像增强，也不是只在离线 tensor 上改 action label。

**为什么需要 perturb：**

```text
同一局部状态附近
→ 执行略有差异的 action chunks
→ 产生成功、失败和次优结果
→ critic 学到局部动作方向差异
```

**数据规模：**

```text
300 episodes
60,505 transitions
36 reset states contain both success and failure outcomes
```

**Chunk transition 构造：**

每个时刻缓存：

```text
compact prefix feature zₛ
8D proprioception pₛ
5 × 7 executable action chunk Aₜ
reward / return / done
next-state feature zₛ₊ₕ
Base reference chunk at the next state
valid-action mask near episode termination
```

**核心画面：**

```text
episode trajectory
    ↓ sliding chunk window H=5
[aₜ, aₜ₊₁, aₜ₊₂, aₜ₊₃, aₜ₊₄]
    ↓
(state, action chunk, return, next state)
```

**核心句：**

```text
Perturbation creates nearby action-outcome supervision; chunking turns it into Q-learning data.
```

---

## 幻灯片 7：三种 Q 策略总览

**时间：** `01:39–01:59`

**标题：**

```text
Three Q-learning strategies for SmolVLA
```

**画面结构：** 使用三张并列卡片。

### 方式一：Q selection——“挑动作”

```text
Sample N action chunks
→ score each chunk with Q
→ execute the highest-Q candidate
```

- 不修改 policy 权重。
- 推理时需要 critic。
- 依赖 critic 对候选 chunk 的排序能力。

### 方式二：Q guidance——“改动作”

```text
Base action chunk
→ bounded gradient ascent on Q
→ projected guided action
```

- 不修改 policy 权重。
- 推理时需要 critic 与 Q-gradient。
- 直接利用 `∇A Q(s,A)` 改变动作方向。
- 使用步数、步长、最大偏移和 gate 约束。

### 方式三：QVGM residual——“写进策略”

```text
Critic-improved clean action
→ residual velocity target
→ fine-tune Action Expert offline
→ deploy without critic
```

- 离线训练 residual policy，因此会更新 Action Expert。
- 把 clean-action 改进转换为 flow velocity residual supervision。
- 部署时不需要 critic，推理接口与 Base 相同。

**三者核心区别：**

| 方法 | 是否重训 policy | 部署是否需要 critic | 改进作用位置 |
|---|---|---|---|
| Q selection | 否 | 是 | 候选之间选择 |
| Q guidance | 否 | 是 | 测试时直接修改动作 |
| QVGM residual | 是，离线更新 Action Expert | 否 | 蒸馏到 velocity field |

---

## 幻灯片 8：冻结的四路配对评测协议

**时间：** `01:59–02:13`

**标题：**

```text
One protocol, four policy-improvement paths
```

**评测路线：**

```text
Base
Q selection, N=4
Q guidance
QVGM residual policy
```

**固定条件：**

```text
50 reset states
Seed 2001
240 max steps
5 actions per replan
Same task and Base checkpoint
```

**主要内容：**

- 同一个 reset state 分别运行四条路线。
- 使用 paired outcome 判断改善和回退。
- 使用 exact McNemar test，而不只比较两个总体成功率。

---

## 幻灯片 9：同状态闭环行为对比

**时间：** `02:13–02:31`

**标题：**

```text
Same reset. Same seed. Different outcome.
```

**画面：**

- 左侧：Base 的 LIBERO 闭环仿真录像，最终 `FAILURE`。
- 右侧：Q-guidance 的 LIBERO 闭环仿真录像，最终 `SUCCESS`。
- 同步播放，同一 reset state、seed 和速度。

**案例：**

```text
LIBERO-Spatial Task 7
Reset state 1
Seed 2001
```

**核心信息：**

```text
Q-guidance changes the action—not the policy weights.
```

---

## 幻灯片 10：三种 Q 策略的核心结果

**时间：** `02:31–02:53`

**标题：**

```text
Action-direction improvement outperforms candidate selection
```

**核心结果表：**

| 方法 | Success | 相对 Base | 配对变化 | Exact McNemar |
|---|---:|---:|---|---:|
| Base | `21/50 (42%)` | — | — | — |
| Q selection, N=4 | `18/50 (36%)` | `−3` | 0 改善 / 3 回退 | `0.25` |
| **Q guidance** | **`34/50 (68%)`** | **`+13`** | 19 改善 / 6 回退 | **`0.0146`** |
| QVGM residual | `32/50 (64%)` | `+11` | 11 改善 / 0 回退 | `0.00098` |

**核心结论：**

1. Q selection 没有帮助：critic 对候选排序的微小差异没有转化为闭环收益。
2. Q guidance 最强：直接沿动作价值梯度修正动作，达到最高成功率。
3. QVGM residual 略低于 guidance，但实现零配对回退，且部署时不需要 critic。

**主标题数字：**

```text
Q-guidance: 42% → 68%
+13 net states · +26 percentage points
```

---

## 幻灯片 11：第二任务复现实验

**时间：** `02:53–03:13`

**标题：**

```text
Same method ranking on a second LIBERO task
```

**Task 7 主实验：**

| Base | Q selection | Q guidance | QVGM residual |
|---:|---:|---:|---:|
| `42%` | `36%` | **`68%`** | `64%` |

**Task 3 diagnostic replication：**

| Base | Q selection | Q guidance | QVGM residual |
|---:|---:|---:|---:|
| `76%` | `70%` | **`88%`** | `86%` |

**配对结果：**

```text
Q-guidance: 6 improvements · 0 regressions · exact p = 0.03125
```

**必须同时展示的边界：**

```text
Held-out TD loss: 0.0121 > 0.01 gate
Conservative preset: 5 steps / 0.005 step size / 0.02 max delta
Diagnostic replication—not a second primary result
```

**核心结论：**

- 两个任务上的方法排序相同：guidance 第一、residual 第二、selection 低于 Base。
- Task 3 的 Base 已有 `76%`，说明 guidance 并非只对弱 Base 有效。
- 由于 Task 3 critic 略微未通过预设 TD gate，只能称为 diagnostic replication。
- 结论仍限定在两个 LIBERO-Spatial 任务，不能推广到所有任务或真实机器人。

---

## 幻灯片 12：AMD Radeon Attention Profiling

**时间：** `03:13–03:30`

**标题：**

```text
Built and profiled on AMD Radeon PRO
```

**硬件：**

```text
Radeon PRO W7000 Series · 48 GiB VRAM
gfx1100 architecture · 96 CUs
PyTorch 2.8.0+rocm6.4
ROCm runtime 7.2.4
```

**同页三张图：**

1. Forward throughput。
2. Backward throughput。
3. FWD+BWD 完整 step 时间。

**结论：**

```text
CK dominates long-sequence forward throughput.
SDPA is faster for backward and complete training steps.
```

**脚注：**

```text
Kernel microbenchmark · B=8 · H=16 · D=64 · causal FP16
```

---

## 幻灯片 13：策略推理延迟优化

**时间：** `03:30–03:49`

**标题：**

```text
10.1% lower policy latency without retraining
```

**核心数字：**

```text
Baseline:   321.8 ms/replan
Optimized:  289.3 ms/replan

10.1% lower latency
1.112× speedup
```

**优化内容：**

- Auto fused SDPA on ROCm。
- Inference mode。
- 固定 denoising loop，避免 GPU scalar 条件同步。
- 缓存语言 token 与 model layer 引用。
- 纯动作部署使用 lightweight output。

`denoising layout cache` 是冻结 `10.1%` 结果之后的独立增量实验，不归因到本页
主数字；其额外收益约为 `0.31%`。

**误差：**

```text
Maximum action difference: 9.3e−4
Mean action difference: 1.8e−4
```

**上游贡献小卡片：**

```text
Upstream-ready LeRobot extensions
• ROCm-aware SDPA and FA-CK paths
• SmolVLA mask compatibility
• Reproducible latency benchmark
• Opt-in inference caches and rollback switches
```

---

## 幻灯片 14：100 分评分证据对应

**时间：** `03:49–04:01`

**标题：**

```text
Judging Criteria Alignment
Evidence mapped across the 100-point rubric
```

| 评分项 | 分值 | Q-Forge 证据 |
|---|---:|---|
| Robot capability | 30 | Task 7 guidance `42% → 68%`；Task 3 diagnostic replication `76% → 88%` |
| AMD Radeon / ROCm | 20 | Radeon PRO W7000 Series 全流程、kernel profiling、`10.1%` policy latency reduction |
| Innovation | 20 | selection、guidance、velocity residual 三条 Q-learning 路线 |
| Real-world value | 20 | 复用失败 rollout，无需新增专家标注；guidance 无需重训；residual 部署免 critic |
| Upstream open source | 10 | LeRobot AMD backend、mask 支持、benchmark 和 rollback switches |

**开源措辞：**

```text
Prepared for upstream contribution
```

在真实 PR 创建或合并前，不写 `merged upstream`。

---

## 幻灯片 15：结论与提交信息

**时间：** `04:01–04:15`

**标题：**

```text
Q-Forge
Value learning for flow-matching Physical AI
```

**三个结论卡片：**

```text
Three Q-learning paths
Selection · Guidance · Residual
```

```text
Best result: Q-guidance
34 / 50 · 68% · p=0.0146
```

```text
AMD-aware deployment
10.1% lower policy latency
```

**一句话总结：**

```text
Q-Forge shows that value learning can improve a flow-matching SmolVLA policy
from its own experience, with Q-guidance providing the strongest no-retraining result.
```

**提交信息：**

```text
Project: Q-Forge
Team: Cao Yuhao
Track 3: Physical AI
GitHub: ZorAttC
```

## 三种 Q 策略必须讲准确的边界

### Q selection

- 不训练 policy。
- 推理时需要多次采样 policy，并由 critic 排序。
- 当前结果为 `18/50`，没有提升 Base。
- 结论不是“Q critic 无效”，而是“当前 critic 的候选间排序信号不足以带来闭环改善”。

### Q guidance

- 不训练或修改 policy 权重。
- 从 Base action 出发，用受约束 Q-gradient 直接修正动作。
- 推理时需要 critic。
- 当前最强结果为 `34/50`。
- “稳定”限定为当前评测的数据规模与冻结协议，不推广到所有场景。

### QVGM residual

- 需要离线训练 Action Expert，因此不能说“完全无需重训 policy”。
- 它把 critic-guided clean-action displacement 转换为 velocity residual target。
- 部署时不需要 critic。
- 当前结果为 `32/50`，有 11 次改善、0 次回退。
- 其价值在于把测试时指导摊销进 policy，而不是取得最高成功率。

## 视频最终需要建立的项目认知

```text
Q-Forge 不是单一 Q-guidance 技巧，
而是在 SmolVLA 上对三种 value-based policy improvement 路线的系统探索。

Q selection 说明仅靠“挑采样”不足；
Q guidance 说明动作方向梯度可以稳定改善当前策略；
QVGM residual 说明价值改进可以离线蒸馏进 flow velocity field。
```
