**A Complete, Interactive-First Reinforcement Learning Curriculum — From MDPs to RLHF**

This curriculum assumes **no prior RL background**, but it expects comfort with linear algebra, probability, and basic calculus. Every chapter is written blog-style with LaTeX derivations, at least one **interactive visualizer**, a **quiz**, and a short coding exercise. Part V contains clearly marked **projects**. The sequence is designed so that each part depends only on the previous ones, but Parts III–V can be reordered after Part II depending on whether you are more interested in control, LLMs, or decision-making under uncertainty.

---

## Part I — Foundations: The Language of Sequential Decision Making

### Chapter 1. What Reinforcement Learning Really Is
- The agent–environment loop; states, actions, rewards, transitions, policies.
- **Evaluative vs. instructive feedback**; why supervised learning is not enough.
- The exploration–exploitation dilemma stated mathematically.
- A first taxonomy: model-free vs. model-based; on-policy vs. off-policy; online vs. offline.
- **Interactive visualizer:** *Reward-Signal Explorer* — drag reward values on a grid and watch the optimal policy change immediately.
- **Quiz:** Identify the RL elements in a described scenario; distinguish episodic from continuing tasks.

### Chapter 2. Multi-Armed Bandits
- The \(k\)-armed bandit problem; action-value estimates \(Q_t(a)\).
- Sample-average and incremental update: \(Q_{n+1} = Q_n + \alpha(R_n - Q_n)\).
- ε-greedy, optimistic initial values, UCB: \(A_t = \arg\max_a [Q_t(a) + c\sqrt{\ln t / N_t(a)}]\).
- Gradient bandits and softmax policies: \(\pi_t(a) = e^{H_t(a)} / \sum_b e^{H_t(b)}\).
- **Contextual bandits** as the bridge to full RL.
- **Interactive visualizer:** *Bandit Arena* — run ε-greedy, UCB, and Thompson sampling side-by-side on a 10-armed testbed; see regret curves update in real time.
- **Quiz:** Derive the UCB bonus from Hoeffding’s inequality; explain why optimistic initialization drives exploration.

### Chapter 3. Markov Decision Processes
- The MDP tuple \((\mathcal{S}, \mathcal{A}, P, R, \gamma)\); Markov property.
- Returns: \(G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}\).
- Value functions: \(v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t=s]\), \(q_\pi(s,a)\).
- **Bellman expectation equations**: \(v_\pi(s) = \sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')]\).
- **Bellman optimality equations**: \(v_*(s) = \max_a \sum_{s',r} p(s',r|s,a)[r + \gamma v_*(s')]\).
- Optimal policies and the existence of deterministic optimal policies.
- **Interactive visualizer:** *MDP Explorer* — build a gridworld, set transition probabilities and rewards, and watch value functions propagate through the Bellman backup.
- **Quiz:** Write the Bellman optimality equation for \(q_*\); prove that any policy greedy with respect to \(v_*\) is optimal.

---

## Part II — Exact and Sample-Based Tabular Methods

### Chapter 4. Dynamic Programming
- Policy evaluation (prediction) via iterative Bellman backups.
- Policy improvement theorem; **policy iteration**.
- **Value iteration**: \(v_{k+1}(s) = \max_a \sum_{s',r} p(s',r|s,a)[r + \gamma v_k(s')]\).
- Asynchronous DP; generalized policy iteration (GPI).
- Convergence and contraction mapping arguments.
- **Interactive visualizer:** *Policy Iteration Sandbox* — step through evaluation and improvement on a 5×5 grid; see convergence of \(\|v_{k+1}-v_k\|_\infty\) in real time.
- **Quiz:** Show that the Bellman optimality operator is a \(\gamma\)-contraction in the sup norm.

### Chapter 5. Monte Carlo Methods
- MC prediction: averaging returns from sampled episodes.
- MC control with exploring starts; ε-soft policies.
- **Off-policy MC** via importance sampling:
\[
\rho_{t:T-1} = \prod_{k=t}^{T-1} \frac{\pi(A_k|S_k)}{b(A_k|S_k)}.
\]
- Incremental importance sampling; weighted importance sampling.
- **Interactive visualizer:** *Episode Replay* — sample trajectories from a stochastic gridworld and watch the running return average converge; toggle on/off-policy and see the variance difference.
- **Quiz:** Derive the importance-sampling estimator for \(v_\pi(s)\); explain why weighted IS has lower variance.

### Chapter 6. Temporal-Difference Learning
- **TD(0)**: \(V(S_t) \leftarrow V(S_t) + \alpha[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]\).
- TD error \(\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)\).
- **Sarsa** (on-policy TD control) and **Q-learning** (off-policy TD control):
\[
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha[R_{t+1} + \gamma \max_a Q(S_{t+1},a) - Q(S_t,A_t)].
\]
- Maximization bias; **Double Q-learning**.
- **Interactive visualizer:** *TD Cliff Walk* — compare Sarsa and Q-learning on the cliff-walking task; see the learned paths and the online return curves diverge.
- **Quiz:** Explain the difference between the Sarsa and Q-learning targets; construct a scenario where maximization bias causes failure.

### Chapter 7. \(n\)-Step Bootstrapping and Eligibility Traces
- \(n\)-step returns: \(G_{t:t+n} = \sum_{k=0}^{n-1} \gamma^k R_{t+k+1} + \gamma^n V(S_{t+n})\).
- \(n\)-step Sarsa and \(n\)-step off-policy learning.
- **TD(\(\lambda\))** and eligibility traces:
\[
E_t(s) = \gamma \lambda E_{t-1}(s) + \mathbf{1}(S_t = s).
\]
- Forward and backward views; Sarsa(\(\lambda\)) and Watkins’ Q(\(\lambda\)).
- **Interactive visualizer:** *Trace Propagation* — on a gridworld, watch eligibility traces “light up” along a trajectory and see how \(\lambda\) controls the credit-assignment horizon.
- **Quiz:** Derive the offline \(\lambda\)-return and show it equals the forward view.

### Chapter 8. Planning and Learning with Tabular Methods
- Models and planning; **Dyna** architecture: acting, learning, and planning in the same loop.
- Prioritized sweeping; trajectory sampling.
- **MCTS** basics: selection, expansion, simulation, backup.
- **Interactive visualizer:** *Dyna Gridworld* — toggle planning steps on/off and watch sample efficiency change; compare Dyna-Q with vanilla Q-learning.
- **Quiz:** Explain why Dyna can be more sample-efficient than Q-learning; derive the prioritized sweeping priority \(p = |R + \gamma \max_a Q(S',a) - Q(S,A)|\).

---

## Part III — Function Approximation and Deep Reinforcement Learning

### Chapter 9. Function Approximation
- Why tabular methods fail in large state spaces.
- Parametric value functions \(v_\theta(s)\) and \(q_\theta(s,a)\).
- **Semi-gradient TD(0)**:
\[
\theta_{t+1} = \theta_t + \alpha[R_{t+1} + \gamma v_\theta(S_{t+1}) - v_\theta(S_t)]\nabla_\theta v_\theta(S_t).
\]
- The **deadly triad**: function approximation + bootstrapping + off-policy learning.
- Linear function approximation and convergence guarantees.
- **Interactive visualizer:** *Value Surface Fitting* — fit a linear or polynomial value function to a continuous-state task and watch the TD error surface shrink.
- **Quiz:** Explain why off-policy TD with nonlinear function approximation can diverge; give the Baird counterexample.

### Chapter 10. Deep Q-Networks and Value-Based Deep RL
- **DQN**: experience replay, target networks, and the loss:
\[
L(\theta) = \mathbb{E}_{(s,a,r,s')\sim \mathcal{D}}\left[\left(r + \gamma \max_{a'} Q_{\theta^-}(s',a') - Q_\theta(s,a)\right)^2\right].
\]
- **Double DQN**, **Dueling DQN**, **Prioritized Experience Replay**.
- **Distributional DQN**: C51, QR-DQN, IQN — learning \(Z(s,a)\) instead of \(\mathbb{E}[Z]\).
- **Interactive visualizer:** *DQN Training Dashboard* — train DQN on CartPole in the browser; watch the Q-value heatmap evolve, the replay buffer fill, and the target network lag.
- **Quiz:** Derive the Double DQN target; explain how distributional RL enables risk-sensitive policies.

### Chapter 11. Policy Gradient Methods
- The policy gradient theorem:
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\left[\nabla_\theta \log \pi_\theta(A_t|S_t) \, \hat{q}(S_t,A_t)\right].
\]
- **REINFORCE** with baseline; variance reduction.
- **Actor–critic** architecture: \(A(s,a) = Q(s,a) - V(s)\).
- Advantage estimation; **GAE(\(\lambda\))**.
- **Interactive visualizer:** *Policy Gradient Playground* — run REINFORCE on a 2D navigation task; see the policy distribution rotate toward high-reward actions step by step.
- **Quiz:** Prove the policy gradient theorem for the episodic case; show that subtracting a state-dependent baseline does not introduce bias.

### Chapter 12. Trust-Region and Proximal Policy Optimization
- **TRPO**: constrained policy update with KL divergence:
\[
\max_\theta \mathbb{E}\left[\frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} A(s,a)\right] \quad \text{s.t.} \quad \mathbb{E}[D_{\mathrm{KL}}(\pi_{\theta_{\text{old}}} \| \pi_\theta)] \le \delta.
\]
- **PPO** clipped objective:
\[
L^{\text{CLIP}}(\theta) = \mathbb{E}\left[\min\left(r_t(\theta)A_t, \operatorname{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right].
\]
- Practical tricks: advantage normalization, entropy bonus, learning-rate annealing.
- **Interactive visualizer:** *PPO Clip Visualizer* — drag the probability ratio \(r_t(\theta)\) and advantage \(A_t\) to see exactly when the clipped objective activates and why it prevents destructive updates.
- **Quiz:** Derive the PPO gradient; explain why clipping is a first-order approximation to a trust region.

---

## Part IV — Modern and Advanced Topics

### Chapter 13. Model-Based Reinforcement Learning
- Learning a dynamics model \(\hat{P}(s'|s,a)\) and reward model \(\hat{R}(s,a)\).
- **Dyna-style** planning with learned models; **MPC** and shooting methods.
- **PETS**, **MBPO**, **Dreamer** (latent world models + imagination).
- **MuZero**: learned latent model + MCTS, no explicit rules.
- **Interactive visualizer:** *World-Model Rollout* — train a tiny dynamics model on a pendulum and watch imagined trajectories diverge from real ones as the horizon grows; adjust the model capacity and see the compounding error.
- **Quiz:** Derive the model-based policy gradient; explain the bias–variance trade-off between model-based and model-free returns.

### Chapter 14. Offline Reinforcement Learning
- The **distribution shift** problem: \(\pi(a|s) > 0\) where \(\mu(a|s) \approx 0\).
- **BCQ**, **CQL** (conservative Q-learning), **IQL** (implicit Q-learning without OOD queries), **AWAC**, **TD3+BC**.
- Model-based offline RL; sequence modeling approaches (Decision Transformer).
- Evaluation without online interaction.
- **Interactive visualizer:** *Offline Data Explorer* — load a fixed dataset from a gridworld and compare the Q-values learned by naive DQN, CQL, and IQL on out-of-distribution actions.
- **Quiz:** Explain why CQL penalizes OOD actions; derive the IQL loss and show why it never queries \(Q(s,a')\) for \(a' \notin \mathcal{D}\).

### Chapter 15. Exploration and Intrinsic Motivation
- Count-based exploration and pseudo-counts.
- **Intrinsic Curiosity Module (ICM)**: forward model prediction error as reward.
- **Random Network Distillation (RND)**.
- **Never Give Up** and episodic novelty.
- **Interactive visualizer:** *Curiosity Explorer* — navigate a sparse-reward maze with and without an intrinsic reward; see which regions the agent visits and how the exploration bonus decays.
- **Quiz:** Derive the ICM intrinsic reward; explain why a forward model alone can be gamed by stochasticity and how the inverse model fixes it.

### Chapter 16. Hierarchical Reinforcement Learning
- The **options framework**: temporally extended actions \((I_o, \pi_o, \beta_o)\).
- High-level policy over options; option-critic architecture.
- **Feudal RL** and goal-conditioned hierarchies.
- **Interactive visualizer:** *Option Composition* — build a two-room gridworld where low-level options (go-to-door, go-to-key) are learned first, then a high-level policy composes them; toggle the hierarchy on/off and compare learning curves.
- **Quiz:** Write the option-value Bellman equation; show that options can accelerate learning by propagating value over longer temporal scales.

### Chapter 17. Multi-Agent Reinforcement Learning
- Markov games; cooperative, competitive, and mixed settings.
- **MADDPG** (centralized training, decentralized execution); **QMIX** for value factorization.
- **MAPPO** and parameter sharing.
- Non-stationarity and equilibrium selection.
- **Interactive visualizer:** *Cooperative Navigation* — two agents learn to cover landmarks; toggle independent PPO vs. MAPPO with a shared critic and watch coordination emerge.
- **Quiz:** Explain the CTDE paradigm; derive the QMIX monotonicity constraint and why it enables decentralized greedy action selection.

### Chapter 18. Meta-Reinforcement Learning and Multi-Task RL
- **Meta-RL** problem formulation: learn to adapt to a distribution of tasks.
- Recurrent meta-RL (RL²); gradient-based meta-RL (MAML-style).
- **Goal-conditioned policies** and hindsight experience replay (HER).
- Task inference and context variables.
- **Interactive visualizer:** *Few-Shot Adaptation* — train a meta-RL agent on a family of point-mass reaching tasks; at test time, show the within-episode adaptation curve on a held-out task.
- **Quiz:** Write the meta-RL objective; explain why a recurrent policy can implement adaptation without gradient steps.

### Chapter 19. Distributional and Risk-Sensitive RL
- Return distributions \(Z^\pi(s,a)\); distributional Bellman operator.
- **C51**, **QR-DQN**, **IQN** — representing full distributions.
- Risk measures: CVaR, mean–variance, distorted expectations.
- Risk-sensitive policy gradients.
- **Interactive visualizer:** *Risk Profile Explorer* — train a distributional agent on a risky asset-allocation task; drag the risk distortion parameter \(\tau\) and see how the policy shifts from risk-seeking to risk-averse.
- **Quiz:** Derive the distributional Bellman equation; show how CVaR can be computed from a quantile representation.

### Chapter 20. Imitation Learning and Inverse Reinforcement Learning
- **Behavioral cloning** and its compounding-error problem.
- **DAgger** (dataset aggregation).
- **Inverse RL**: recover a reward function from demonstrations (MaxEnt IRL, GAIL).
- Adversarial imitation; IQ-learn.
- **Interactive visualizer:** *Reward Recovery* — watch an IRL algorithm infer a reward map from expert trajectories in a gridworld; compare the recovered reward to the ground truth.
- **Quiz:** Derive the MaxEnt IRL objective; explain why behavioral cloning fails when the expert’s state distribution differs from the learner’s.

### Chapter 21. Safe and Constrained RL
- **Constrained MDPs (CMDPs)**: maximize reward subject to \(\mathbb{E}[\sum c_t] \le d\).
- Lagrangian methods; CPO; primal–dual updates.
- **Shielding** and model-based safety guarantees.
- Curriculum induction for safe exploration.
- **Interactive visualizer:** *Safety Budget* — a car must reach a goal while keeping collision probability below a slider-controlled budget; watch the policy become more conservative as the budget tightens.
- **Quiz:** Write the Lagrangian for a CMDP; explain why the dual variable can be interpreted as a “price of safety.”

### Chapter 22. Reinforcement Learning from Human Feedback and LLM Alignment
- **RLHF pipeline**: supervised fine-tuning → reward modeling (Bradley–Terry) → PPO alignment.
- **DPO**: direct preference optimization without an explicit reward model:
\[
\mathcal{L}_{\text{DPO}} = -\mathbb{E}_{(x,y_w,y_l)}\left[\log \sigma\left(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)\right].
\]
- **GRPO** (group relative policy optimization) and **RLVR** (RL with verifiable rewards).
- Reward hacking, KL drift, and evaluation.
- **Interactive visualizer:** *Preference Landscape* — visualize the implicit reward \(\beta \log(\pi_\theta/\pi_{\text{ref}})\) on a 2D preference dataset; drag \(\beta\) and see the DPO policy shift.
- **Quiz:** Derive DPO from the RLHF objective; explain how GRPO removes the critic by using group-relative advantages.

---

## Part V — Projects (Clearly Marked)

### Project 1. Tabular RL from Scratch
Implement value iteration, policy iteration, MC control, Sarsa, and Q-learning on a custom gridworld. Compare sample efficiency and wall-clock time. Add eligibility traces and Dyna. **Deliverable:** a blog post with convergence plots and an interactive trace viewer.

### Project 2. Deep RL on a Continuous-Control Task
Implement DDPG, TD3, and SAC on MuJoCo or PyBullet. Ablate target policy smoothing, twin critics, and entropy temperature. **Deliverable:** a reproducible report with learning curves and a video of the learned policy.

### Project 3. Offline RL Benchmark
Train CQL, IQL, and BCQ on D4RL datasets. Evaluate offline and after fine-tuning. **Deliverable:** a leaderboard-style comparison with OOD action analysis.

### Project 4. Model-Based World Model
Implement DreamerV3 or a simplified latent world model on a pixel-based environment. Visualize imagined rollouts and compare sample efficiency against PPO. **Deliverable:** an interactive notebook where readers can perturb the latent state and see the imagined trajectory change.

### Project 5. RLHF/DPO Alignment Mini-Pipeline
Fine-tune a small language model with DPO on a preference dataset. Compare against PPO-RLHF. Measure KL divergence, reward margin, and generation quality. **Deliverable:** a blog post with before/after samples and an interactive preference slider.

### Project 6. Multi-Agent Coordination
Train MAPPO and QMIX on a cooperative multi-agent benchmark (e.g., SMAC or PettingZoo). Analyze coordination emergence and robustness to agent dropout. **Deliverable:** a visualization of joint policies and communication patterns.

---
