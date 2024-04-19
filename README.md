# tg reviewer bot

Telegram 投稿/审稿机器人，基于 Telegram Bot API 7.1 以及 python-telegram-bot v21.0.1

## 功能使用方法

### 投稿

1. 与机器人私聊，使用 `/new` 命令开始一个新的提交。
2. 按照提示发送您希望投稿的内容，包括文本、图片、视频和文件。
3. 可以实名或匿名提交、取消当前的提交。
4. 支持多次发送内容合并到同一个投稿。

### 审稿

1. 投稿消息将发送到指定的审核群组。
2. 审核人员可以通过投票按钮通过或拒绝投稿。
3. 投稿被拒绝后，需要由拒稿人提供拒绝理由。
4. 支持在审稿结束前撤回投票。
5. 支持附加审稿人备注到稿件，若稿件通过将会附加到通过的稿件末尾
6. 支持审稿人通过机器人向投稿人发送消息。
7. 支持对 NSFW 稿件自动添加遮罩。

### 用户屏蔽

1. 在审稿群中使用 `/ban 用户uid 理由` 屏蔽特定用户投稿
2. 在审稿群中使用 `/unban 用户uid` 解除屏蔽
3. 在审稿群中使用 `/listban` 查看被屏蔽的用户列表
4. 被屏蔽的用户无法新建投稿，可通过 `TG_BANNED_NOTIFY` 环境变量设置是否需要对该用户进行被屏蔽的提示
5. 被屏蔽的用户信息（用户名、全名）根据屏蔽时的 uid 获取并存于数据库，不会实时更新（避免用户拉黑机器人后无法获取最新的用户名），管理员的用户信息则是实时获取（因此需要管理员都曾与机器人聊天过）

### 统计

1. 统计投稿者投稿数、被采纳数与被拒数，并可由投稿者通过机器人发送 `/stats` 获取或者由审稿人在审稿群中发送 `/stats uid` 获取
2. 统计审稿人通过数、拒绝数、通过后被其他审稿人拒绝的数量、拒绝后被其他审稿人通过的数量，由审稿人在审稿群中发送 `/reviewer_stats uid` 获取

## 环境变量

以下是项目中使用的环境变量及其含义的详细列表：

| 环境变量名称                 | 描述                                      | 示例值                                 | 是否必须                                                       |
| ---------------------------- | ----------------------------------------- | -------------------------------------- | -------------------------------------------------------------- |
| `TG_TOKEN`                   | Telegram 机器人的 API 令牌                | `123456789:ABCdefGhIJKlmNopQRSTuvwxYz` | 是                                                             |
| `TG_REVIEWER_GROUP`          | 审稿群组的 ID，用于发送审稿消息           | `123456789`                            | 是                                                             |
| `TG_PUBLISH_CHANNEL`         | 发布投稿频道的 ID，用于发布审核通过的投稿 | `123456789`                            | 是                                                             |
| `TG_REJECTED_CHANNEL`        | 被拒绝投稿的频道 ID，用于发送被拒绝的内容 | `123456789`                            | 否，若不存在则不转发被拒稿件                                   |
| `TG_BOT_USERNAME`            | Telegram 机器人的用户名                   | `my_review_bot`                        | 是                                                             |
| `TG_RETRACT_NOTIFY`          | 是否通知投稿者稿件被撤回                  | `True` 或 `False`                      | 否，默认为 True                                                |
| `TG_APPROVE_NUMBER_REQUIRED` | 通过所需的最小审核人数                    | `2`                                    | 否，默认为 2                                                   |
| `TG_REJECT_NUMBER_REQUIRED`  | 拒稿所需的最小审核人数                    | `2`                                    | 否，默认为 2                                                   |
| `TG_REJECTION_REASON`        | 预置拒绝理由的列表，以冒号分隔            | `"内容不够有趣:内容不适当:重复投稿"`   | 否，若无，则只支持自定义理由和暂无理由因重复而拒稿时的预置理由 |
| `TG_BANNED_NOTIFY`           | 是否通知投稿者已被屏蔽                    | `True` 或 `False`                      | 否，默认为 True                                                |

请确保在使用项目前正确设置这些环境变量，以保证程序的正常运行。对于标记为“是”的变量，它们是项目运行所必需的，而对于标记为“否”的变量，则为可选配置，如果未设置，项目将使用默认值或不执行相关功能。

## 安装与部署

设置环境变量，安装 `python-telegram-bot v21.0.1` 库，运行 `main.py` 文件即可。代码使用 python3 编写。

## 技术支持与贡献

如果您在使用过程中遇到任何问题，或者希望为项目贡献代码，请通过 GitHub 的 issue 或 pull request 与我们联系。

## 许可证

本项目使用 GPLv3 许可证。
