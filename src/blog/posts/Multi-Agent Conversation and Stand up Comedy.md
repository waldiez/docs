---
date: 2024-11-02
updated: 2025-01-31
readtime: 15
categories:
  - Standup Comedians
authors:
  - waldiez
---

![Example 1 overview](../../static/images/light/examples/1/overview.webp#only-light)
![Example 1 overview](../../static/images/dark/examples/1/overview.webp#only-dark)

This guide walks you through creating a conversational flow in JupyterLab using the Waldiez extension, where two agents, "Joe" and "Cathy," simulate a standup comedy exchange. We will configure an OpenAI model (GPT-3.5-turbo) for this flow and observe the interaction between the agents.

<!-- more -->

---

## Using user input to start the conversation

In this example, we will set up a flow where the user initiates the conversation by providing an initial message. The agents, Joe and Cathy, will then respond to each other based on the user input and the previous agent's message.

### Open JupyterLab and Launch Waldiez

1. Start **JupyterLab**.
2. In the launcher, under the **Waldiez** section, select the Waldiez icon to create a new `.waldiez` file. This opens a new interface for setting up agents and configuring the flow.

---

### Add a Model

1. In the Waldiez interface, click on `Add model` to add a new model configuration.
2. Fill out the configuration fields:
   - **Name**: `gpt-3.5-turbo`
   - **Model Type**: Select `OpenAI`.
   - **API Key**: Enter your OpenAI API key (make sure you have GPT-3.5-turbo access).
3. Optionally adjust **Advanced Settings** like **Temperature** and **Max Tokens** as per your needs.
4. Click **Save** to add the model to your flow.

---

### Create Agents

#### Agent 1: Cathy

1. Under the `Agents` section, drag a new agent onto the canvas.
2. Name the agent **Cathy**.
3. Set the description to "Cathy is a standup comedian."
4. In the **System Message** field, enter: `Your name is Cathy and you are a standup comedian.`
5. Link the `gpt-3.5-turbo` model to Cathy by selecting it in the **Models** tab.
6. Save the configuration.

#### Agent 2: Joe

1. Add another agent to the canvas and name it **Joe**.
2. Set the description to "Joe is a standup comedian."
3. In the **System Message** field, enter: `Your name is Joe and you are a standup comedian. Start the next joke from the previous punchline.`
4. Link the `gpt-3.5-turbo` model to Joe.
5. Save the configuration.

---

### Link Agents

1. In the Waldiez canvas, create a chat link between **Joe** and **Cathy**.
2. Click on the link and configure the following settings:
   - **Chat Type**: Leave this as is: "Chat."
   - **Name**: `Joe => Cathy`.
   - **Max Turns**: Specify the number of turns for their exchange (e.g., 3).
3. Click **Save** to apply the settings.

---

### Update the Flow's settings

1. Open the **Edit Flow** settings.
2. Name the flow, e.g., **Standup comedians 1**, and add a description like "Standup comedians with user input."
3. Add the chat link `Joe => Cathy` to the flow sequence to specify the conversation order.
4. Save the flow configuration.

---

### Initiate the Chat

1. Click on the **Run** button to start the flow.
2. Start the flow by providing an initial message in the **User Input** window, such as:

    `Hi Cathy, I'm Joe. Let's keep the jokes rolling!`

3. Click **Submit** to begin the conversation.

---

### Observe the Conversation in Logs

- The **Logs** window will display the real-time exchange between Joe and Cathy, where each agent responds based on the previous joke or statement, simulating a standup comedy routine.

---

### Review and Export Results

- After the conversation, various CSV logs (e.g., `agents.csv`, `chat_completions.csv`) are saved in the file explorer. You can analyze these logs to evaluate the flow and refine the agent interactions.

---

## Skipping user input

To skip user input and directly start the conversation, you can modify the chat link settings to start with a specific message. Set the message type as "Text" and set the desired starting message to the content field.  This way, the agents will begin the conversation without waiting for user input.

![Skip user input Preview](../../static/images/light/examples/1/skip_user_input.webp#only-light)
![Skip user input Preview](../../static/images/dark/examples/1/skip_user_input.webp#only-dark)

## Using a termination condition

You can also disable the "max turns" setting in the chat link and use a termination condition to end the conversation based on specific criteria. Specify the termination settings in each agent's configuration to control the flow's duration and completion.

![No max turns preview 1](../../static/images/light/examples/1/no_max_turns1.webp#only-light)
![No max turns preview 1](../../static/images/dark/examples/1/no_max_turns1.webp#only-dark)

Also, make sure you update the agents' system messages to reflect the termination condition.

![No max turns preview 2](../../static/images/light/examples/1/no_max_turns2.webp#only-light)
![No max turns preview 2](../../static/images/dark/examples/1/no_max_turns2.webp#only-dark)

---

Files used in this example:

- Using User input: [Standup Comedians 1.waldiez](https://github.com/waldiez/examples/blob/main/01%20-%20Standup%20Comedians/Standup%20Comedians%201.waldiez)
- Without user input: [Standup Comedians 2.waldiez](https://github.com/waldiez/examples/blob/main/01%20-%20Standup%20Comedians/Standup%20Comedians%202.waldiez)
- Without user input and max turns (termination): [Standup Comedians 3.waldiez](https://github.com/waldiez/examples/blob/main/01%20-%20Standup%20Comedians/Standup%20Comedians%203.waldiez)
