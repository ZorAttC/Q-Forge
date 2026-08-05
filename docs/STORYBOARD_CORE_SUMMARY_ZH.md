# Q-Forge 演示视频 Storyboard 核心摘要

> **更新：** 按照 Q-VGM 问题动机并完整介绍 Q selection、Q guidance 和
> QVGM residual 三条路线的推荐新版，请使用
> [`STORYBOARD_CORE_SUMMARY_ZH_V2.md`](STORYBOARD_CORE_SUMMARY_ZH_V2.md)。

> 用途：快速确认每张幻灯片放什么内容。  
> 视频总时长：约 4 分 39 秒。  
> 原则：只讲主线，技术细节和完整实验配置放在 README。

## 整体故事线

```text
项目是什么
→ 为什么需要推理时优化
→ Q-Forge 如何工作
→ 同一状态下的真实行为差异
→ 50 个状态的配对结果
→ AMD Radeon 上的实现与推理优化
→ 核心结论
```

## 正式评分标准（100 分）

| 正式评分项 | 分值 | 视频中的主要页面 |
|---|---:|---|
| Robot capability performance | 30 | 幻灯片 4、6、7、8 |
| AMD Radeon GPU and ROCm adoption | 20 | 幻灯片 9、10 |
| Innovation and originality | 20 | 幻灯片 3、5、10 |
| Real-world application value | 20 | 幻灯片 1、2、3、6 |
| Contributions to upstream open-source projects | 10 | 幻灯片 5、9、10 |

视频应优先保证 30 分的机器人能力结果和 20 分的 AMD/ROCm 采用证据足够醒目，
同时明确展示 Q-Forge 的原创方法、实际应用价值和可提交给 LeRobot 上游的代码贡献。
各页不单独显示评分标签，所有评分映射集中在倒数第二张幻灯片中总结。

## 幻灯片 1：项目标题

**时间：** `00:00–00:18`

**标题：**

```text
Q-Forge
Value-Guided Action Refinement for Physical AI
```

**主要内容：**

- Q-Forge 是一个面向 Physical AI 的推理时动作优化方法。
- 在不重新训练 SmolVLA 的情况下，使用 Q critic 改善动作选择。
- 画面右侧展示真实 LIBERO 机器人场景。
- 使用蓝色 Base 轨迹和绿色 Guided 轨迹表现“失败”和“成功”。

**底部信息：**

```text
AMD Hackathon 2026 · Track 3: Physical AI
Cao Yuhao · Q-Forge
```

---

## 幻灯片 2：Physical AI 问题

**时间：** `00:18–00:42`

**标题：**

```text
A capable policy can still choose the wrong action chunk
```

**主要内容：**

- 一个已经具备基本能力的机器人策略，仍可能在关键状态选错动作 chunk。
- 展示一个 observation 和多个候选动作。
- Q critic 对候选动作进行相对评分。
- 最高价值动作使用绿色高亮。

**必须说明：**

```text
策略 checkpoint 保持冻结，只改变推理时的动作选择。
```

---

## 幻灯片 3：为什么使用推理时 Q-guidance

**时间：** `00:42–01:10`

**标题：**

```text
Improve behavior without retraining the policy
```

**主要内容：**

- 对比三种路线：重新训练、Q selection、Q-guidance。
- 重新训练成本高，不是本项目重点。
- Q selection 比较保守，只从候选中选择。
- Q-guidance 对 Base action chunk 做有约束的小幅优化。
- 最终方案是 Q-guidance。

**Gate 说明：**

```text
只有通过 validation gate 的配置才用于正式评测；
gate 失败时只保留保守诊断，不启用该配置。
```

**边界：**

```text
No policy retraining
No online environment gradients
Frozen checkpoint
```

---

## 幻灯片 4：冻结的配对评测协议

**时间：** `01:10–01:38`

**标题：**

```text
A frozen, paired evaluation protocol
```

**核心数字：**

```text
50 个 reset states
固定 seed 2001
最多 240 steps
每次 replan 执行 5 个动作
```

**主要内容：**

- 每个 reset state 都分别运行 Base 和 Q-guidance。
- 两边使用相同 checkpoint、初始状态、任务和 seed。
- 强调结果来自配对比较，而不是挑选两个独立成功率。

**脚注：**

```text
Primary paired study: LIBERO-Spatial task 7, reset states 0–49.
```

---

## 幻灯片 5：Q-Forge 系统架构

**时间：** `01:38–02:20`

**标题：**

```text
Q-Forge: value-guided refinement around a frozen VLA
```

**离线部分：**

```text
Base policy rollouts
→ Perturbed action chunks
→ Q-labeled transitions
→ QVGM critic
```

**推理部分：**

```text
Observation + language
→ Frozen SmolVLA
→ Base action chunk
→ Q-guidance
→ Executable action chunk
```

**Q-guidance 约束：**

- 动作变化范围受限。
- 优化步数受限。
- 只使用 validation-approved configuration。

**核心视觉：**

```text
Q_guided > Q_base
```

---

## 幻灯片 6：同一初始状态的闭环对比

**时间：** `02:20–02:57`

**标题：**

```text
Same reset. Same seed. Different outcome.
```

**主要内容：**

- 左侧播放 Base 真实 LIBERO 闭环视频。
- 右侧播放 Q-guidance 真实闭环视频。
- 两边使用相同 reset state 和 seed，并同步播放。
- Base 最终标记为 `FAILURE`。
- Q-guidance 最终标记为 `SUCCESS`。

**案例信息：**

```text
LIBERO-Spatial Task 7
Reset state 1
Seed 2001
```

---

## 幻灯片 7：50 个状态的核心结果

**时间：** `02:57–03:17`

**标题：**

```text
Q-guidance improves paired success across 50 reset states
```

**核心数字：**

```text
Base:        21 / 50 = 42%
Q-guidance:  34 / 50 = 68%

+13 successes
+26 percentage points
```

**配对结果：**

```text
Failure → Success: 19
Success → Failure:  6
Unchanged:          25
```

**统计结果：**

```text
Exact McNemar p = 0.0146
```

**核心画面：**

- 使用 50 格矩阵表示 50 个 reset states。
- 绿色表示失败变成功。
- 红色表示成功变失败。
- 灰色或蓝绿色表示结果不变。

---

## 幻灯片 8：成功与失败状态转移

**时间：** `03:17–03:34`

**标题：**

```text
Paired transitions reveal both gains and regressions
```

**主要内容：**

使用 Sankey 图展示：

```text
Base Failure 29
├─ 19 → Q-guidance Success
└─ 10 → Q-guidance Failure

Base Success 21
├─ 15 → Q-guidance Success
└─  6 → Q-guidance Failure
```

**核心结论：**

```text
Net gain: +13 successes
```

**诚实说明：**

```text
Q-guidance 带来显著净改善，但没有完全消除回退。
```

---

## 幻灯片 9：AMD Attention Kernel Benchmark

**时间：** `03:34–03:52`

**标题：**

```text
Built and profiled on AMD Radeon
```

**硬件信息：**

```text
AMD Radeon gfx1100
96 CUs
48 GiB VRAM
PyTorch 2.8 + ROCm 6.4
```

**同一页展示三张图：**

1. Forward throughput。
2. Backward throughput。
3. FWD+BWD 完整 step 时间。

**比较对象：**

- CK FlashAttention。
- Triton FlashAttention。
- PyTorch SDPA。

**结论：**

```text
CK 在长序列 forward attention 中吞吐最高；
SDPA 在 backward 和完整训练 step 中更快。
```

**必须注明：**

```text
Kernel microbenchmark
B=8 · H=16 · D=64 · FP16 causal
```

---

## 幻灯片 10：策略推理延迟优化

**时间：** `03:52–04:10`

**标题：**

```text
10.1% lower policy latency without retraining
```

**核心数字：**

```text
Baseline:   321.8 ms/replan
Optimized:  289.3 ms/replan

Latency reduction: 10.1%
Speedup: 1.112×
Saved: 32.5 ms/replan
```

**主要优化：**

- Auto fused SDPA。
- `torch.inference_mode()`。
- 去除 denoising loop 的逐步 GPU 条件同步。
- 缓存固定任务文本 token。
- 缓存模型层引用。
- 纯动作部署使用 lightweight output。
- 缓存固定 denoising mask 和 position IDs。

**上游开源贡献小卡片：**

```text
LeRobot SmolVLA extensions
• ROCm-aware sdpa_auto backend
• FA-CK mask-compatible inference path
• Inference caches and benchmark scripts
• Reproducible commits prepared for upstream contribution
```

只表述为“prepared for upstream contribution”；在 PR 真正提交或合并前，不写成
“merged upstream”。

**误差说明：**

```text
最大动作差异约 9.3e−4
平均动作差异约 1.8e−4
```

**实验口径：**

```text
固定 observation 和显式 noise
GPU synchronized
30 次测量
报告中位数
只统计 predict_action_batch()
```

**不要展示：**

- LIBERO 环境 step 时间。
- 完整 rollout 总时间。
- 将 attention kernel 加速直接等同于策略加速。

---

## 幻灯片 11：评分点与项目证据对应

**时间：** `04:10–04:24`

**标题：**

```text
Judging Criteria Alignment
100 points of auditable evidence
```

**主要内容：**

使用五行评分对照表，每一行只放评分项、分值和最强证据：

| 评分项 | 分值 | Q-Forge 证据 |
|---|---:|---|
| Robot capability performance | 30 | `21/50 → 34/50`；19 次失败变成功；McNemar `p=0.0146` |
| AMD Radeon GPU and ROCm adoption | 20 | gfx1100 全流程；attention profiling；策略延迟降低 `10.1%` |
| Innovation and originality | 20 | 冻结策略上的 QVGM critic + bounded Q-guidance |
| Real-world application value | 20 | 无需重新训练即可改善已部署 VLA 的关键动作决策 |
| Upstream open-source contributions | 10 | LeRobot AMD/ROCm backend、mask 兼容、benchmark 与可回滚提交 |

**视觉建议：**

- 左侧显示五项分值，形成总计 `100` 的竖向 score bar。
- 右侧每行只显示一个最强证据，不重复技术细节。
- `30` 分机器人能力使用绿色高亮。
- `20` 分 AMD/ROCm 使用红色或 AMD 强调色。
- 其他三项使用统一深色卡片，避免五种颜色造成混乱。
- 页面右上角显示 `Evidence-backed, reproducible, upstream-ready`。

**开源措辞边界：**

```text
Upstream-ready / prepared for upstream contribution
```

在 PR 真正提交或合并前，不写成 `merged upstream` 或 `accepted upstream`。

---

## 幻灯片 12：结论与提交信息

**时间：** `04:24–04:38.6`

**标题：**

```text
Q-Forge
A practical inference-time upgrade for Physical AI
```

**三个核心结论卡片：**

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

**一句话总结：**

```text
A frozen SmolVLA policy, improved through value-guided action refinement and AMD-aware inference.
```

**提交信息：**

```text
Project: Q-Forge
Team: Cao Yuhao
Track 3: Physical AI
GitHub: ZorAttC
```

仓库公开后，在这一页加入 GitHub 短链接和二维码；公开前不要放无效链接。

## 最终必须讲清楚的五点

```text
1. Q-Forge 不重新训练 SmolVLA，而是在推理时用 Q critic 改善动作。
2. 配对成功率从 21/50 提升到 34/50。
3. 有 19 次失败变成功、6 次成功变失败，McNemar p=0.0146。
4. 系统在 AMD Radeon 上完成实现与 profiling，策略延迟降低约 10.1%。
5. 形成了可复用、可复现、准备提交给 LeRobot 上游的 AMD/ROCm 推理扩展。
```

## 内容边界

视频只保留方法主线、真实行为证据、核心统计结果和 AMD 工程贡献。
以下内容放在 README 或提交文档中，不塞进视频：

- 完整 critic 网络结构。
- 所有训练损失和超参数。
- checkpoint 与数据路径。
- 完整 gate 阈值。
- 全部 attention JSON 数据。
- 所有推理环境变量与回滚命令。
- 完整限制与失败分析。
