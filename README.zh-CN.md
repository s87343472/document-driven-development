# 文档驱动开发（Document-Driven Development）

[English](README.md) | **简体中文** | [日本語](README.ja.md) | [Français](README.fr.md)

一个 Claude Code 技能，教会 AI 用文档驱动的方式帮你构建产品。

> 你在 prompt 里省下的十五分钟需求描述，会变成三小时的 debug 账单。**慢在开头，快在全程。**

## 目录

- [什么是文档驱动开发](#什么是文档驱动开发)
- [核心公式](#核心公式)
- [文档体系](#文档体系)
- [安装](#安装)
- [使用方法](#使用方法)
- [效果对比](#效果对比)
- [核心原则](#核心原则)
- [项目结构](#项目结构)
- [最佳实践](#最佳实践)
- [常见问题](#常见问题)
- [系列文章索引](#系列文章索引)
- [更新日志](#更新日志)

## 什么是文档驱动开发

**文档是唯一事实来源（Single Source of Truth）。代码是文档的实现，而不是反过来。**

你对 Agent 说「帮我做注册页面」，它完美实现了它理解的版本——用训练数据的平均值填补了你所有没说出口的假设：安全常识、边界条件、业务规则。自然语言天生模糊，人与人靠共享经验补全，人与 Agent 之间没有这层默契。

这个技能引导你不再让 AI 从模糊需求直接生成代码，而是：

1. **先思考** —— 澄清意图、范围和成功标准
2. **再文档** —— 建立结构化的文档
3. **后编码** —— 基于清晰的规格生成代码

交付物不一定是 web 应用。Skill、Agent、MCP 服务器、CLI 工具、.md 方法论都适用同一套文档体系。

## 核心公式

```
intent.md  →  roadmap.md  →  spec.md  →  plan.md  →  代码
 （为何）      （路径）       （做什么）    （怎么做）
```

- **生成是廉价的，受控演进是稀缺的。** 瓶颈不再是写代码，而是决定什么该存在——文档就是做这个决定的地方。
- **问题追溯到文档。** 代码出错时，先修事实来源，再重新生成。
- **描述你想要什么 ≠ 定义该构建什么。** Spec 负责把前者变成后者。

## 文档体系

| 层级 | 文件 | 回答的问题 | 稳定性 |
| ---- | ---- | ---------- | ------ |
| 意图层 | `intent.md` | 为何做、为谁做 | 很少变化 |
| 路线层 | `roadmap.md` | 版本路径 + 不变的架构主干 | 偶尔变化（仅多版本产品需要） |
| 规格层 | `spec.md` | 做什么 | 随功能变化 |
| 计划层 | `plan.md` | 技术上怎么做 | 经常变化 |

以上是构建期文档。Agentic 产品还可能有**运行时文档**——产品自身在运行中读写的标准 / 记忆 / 状态文件。保持它们版本化且人类可读，让用户能看到、也能修改产品「怎么想」。详见 [`principles.md`](skills/document-driven-development/principles.md)。

## 安装

### Claude Code

```bash
# 项目内
mkdir -p .claude/skills
cp -r skills/document-driven-development .claude/skills/

# 或全局
cp -r skills/document-driven-development ~/.claude/skills/
```

### Claude 网页版 / API

把 `skills/document-driven-development/SKILL.md` 的内容（上下文允许的话加上 `templates.md` 和 `principles.md`）复制进系统提示词或项目指令即可。

## 使用方法

安装后，当你出现以下情况时 Claude 会应用该方法论：

- 明确要求用 DDD 构建项目
- 要求给现有项目添加功能
- 提到 `intent.md`、`spec.md`、`plan.md` 或 `roadmap.md`

注意：技能默认带 `disable-auto-invoke: true` 以避免过度触发。想让它自动激活，删掉 SKILL.md frontmatter 里的这一行即可。

## 效果对比

### 之前：Vibe Coding

```
你：帮我做个个人博客
Claude：好的！[生成 500 行代码]
你：等等，我想要更简单的，不要数据库，就用 markdown 文件……
Claude：哦，我重做一下……[又 500 行，还是不太对]

# 结果：反复迭代，浪费时间，代码和预期不符
```

### 之后：文档驱动

```
你：帮我做个个人博客
Claude：我们用文档驱动开发。先问几个问题：
  1. 主要目的是什么？ 2. 读者是谁？
  3. v0.1 做到什么算「完成」？ 4. 明确不做什么？

你：分享技术文章，读者是开发者。v0.1 只要能渲染 markdown。
    不要评论、不要 CMS、不要数据库。

Claude：[先创建 intent.md、spec.md、plan.md，再生成精准的代码]

# 结果：一次做对，且为后续迭代留下了文档
```

## 核心原则

1. **文档先行，代码在后** —— 没有清晰文档，绝不生成代码
2. **问题追溯到文档** —— 代码出错时，先判断是 spec 问题还是 plan 问题
3. **每个版本一个核心目标** —— v0.1、v0.2、v0.3……小步前进
4. **文档与代码保持同步** —— 一起提交
5. **文档是为了沟通** —— 写给未来的自己和 AI 看
6. **v0.1 之前先定义架构主干** —— 指明跨版本不变的部分，薄版本才不会变成一次性产物
7. **每个版本有验证门** —— 工具的门是「按 spec 工作」；产品的门必须是留存、使用或付费这类真实信号，不是兴趣。门不过，不进下一版
8. **Agentic 项目中，文档可以就是运行时** —— Agent 实时读写文档；保持人类可读、有版本

## 项目结构

```
document-driven-development/
├── README.md               # English
├── README.zh-CN.md         # 简体中文（本文件）
├── README.ja.md            # 日本語
├── README.fr.md            # Français
├── LICENSE
└── skills/
    └── document-driven-development/
        ├── SKILL.md        # 行为规则 + 工作流（省上下文的核心）
        ├── templates.md    # intent / roadmap / spec / plan 模板 + 示例
        └── principles.md   # 哲学、原则 1-8、反模式
```

## 最佳实践

### 应该做

- **从 intent.md 开始** —— 哪怕只有 5 行也比没有强
- **明确写出非目标** —— 「不做用户账号」能防止范围蔓延
- **v0.1 之前命名架构主干** —— 后续版本是填充它，不是重建它
- **保持版本足够小** —— v0.1 应该几小时内可完成，而不是几天
- **需求变了先改文档** —— 修事实来源，不是只改代码
- **文档和代码一起提交**

### 不应该做

- **不要直接跳去写代码** —— 抵抗「先写起来再说」的冲动
- **不要过度文档化** —— plan.md 描述要达成什么，不是逐行代码
- **不要把技术选型写进 spec.md** —— 「用户可以搜索」（对）vs「用 Elasticsearch」（放 plan.md）
- **不要直冲 v1.0** —— v0.1 → v0.2 → v0.3 才是正路
- **不要带着未通过的验证门前进** —— 那是在未经验证的假设上盖楼

## 常见问题

**问：这不是比直接让 AI 写代码更慢吗？**
对琐碎任务，是的。对任何会迭代的东西，不是。写文档花的时间，会在避免「这不是我想要的」循环时成倍收回。

**问：所有文档都必须有吗？**
小项目可以合并，roadmap.md 也只在多版本产品中需要。但分开写能帮你在不同层面思考：为何 → 路径 → 做什么 → 怎么做。

**问：项目中途需求变了怎么办？**
先改文档，再改代码。让文档始终是事实来源。

**问：能配合 Claude 以外的 AI 工具用吗？**
可以。方法论适用于任何 AI 编码助手——把 SKILL.md 复制进系统提示词即可。

## 系列文章索引

本技能提炼自 9 篇系列**「AI 时代的编码新范式」**，基于 43 篇行业文献、学术论文与一线实践报告，探讨 Spec-Driven Development 如何从边缘实践变为工程基础设施：

- [#01 — Vibe Coding 的尽头是规划先行](https://www.sagasu.art/p/vibe-coding-end-is-planning-first)
- [#02 — Specification 即协议：当文档成为代码的「事实来源」](https://www.sagasu.art/p/specification-is-protocol-when-document-becomes-code-fact-source)
- [#03 — 速度的真相：数据告诉你文档驱动到底快不快](https://www.sagasu.art/p/speed-truth-data-document-driven-fast-or-not)
- #04–#09 —— 完整系列见 [sagasu.art](https://www.sagasu.art/)

## 更新日志

- **2026-06** —— 面向 AI 编码工具 / Agent 时代刷新：交付物类型扩展、roadmap.md 桥接层、架构主干原则、逐版本验证门、agentic 项目的文档即运行时（原则 6-8）
- **2026-03** —— 为上下文效率重构：拆分为 SKILL.md + templates.md + principles.md，新增 Stop Condition，收紧触发条件
- **2026-01** —— 首次发布 v1.0

## 贡献

欢迎提交 issue 和 pull request。

## 许可证

MIT License —— 详见 [LICENSE](LICENSE)。

## 作者

**SagaSu**

- 博客：<https://www.sagasu.art/>
- Twitter：[@sujingshen](https://x.com/sujingshen)

## 致谢

基于「文档驱动开发」方法论系列。核心理念：**生成是廉价的，受控演进是稀缺的。**
