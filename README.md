# My Junimo Assistant - AI tool to strategize farming in Stardew Valley

An AI assistent (Junimo) who will give you the best advice for what to work on for the day!

## Using multi-agents

### How to use

1. Recommend to run in a virtual environment
2. In your venv, run `pip install -e .`
3. Config your Gemini API key, LangSmith key in a new `.env` file, see `.env.example`
4. In project root, run `python3 -m my_package.multi_agents.the_foreman`
5. In the prompt `🌱 What would you like to know? (type 'quit' or 'exit' to stop):` type your question, such as "What to do today?" or "What gift should I give to Marnie today?"
6. You can add, save or clear your playstyle preferences following the prompt!
7. Happy farming!

### Functions

#### Plan the day!

```
🌱 What would you like to know? (type 'quit' or 'exit' to stop): What to do today?

-- Start reasoning
🧠 Classifier: Analyzing request and routing...
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
🏡 Farm Status: 127g, spring 3
📋 Routing to: ['money_maker', 'socialite', 'scavenger']
💭 Reasoning: The user's query is a general request for daily activities, which requires input from all specialists to provide a comprehensive plan covering profit, relationships, and item collection.
💰 Money Maker: Analyzing farm economics...
👥 Socialite: Checking relationships and events...
🔍 Scavenger: Searching for quests and bundles...
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
  📚 Found related Wiki context of length 1437 in SV Wiki
  📚 Found related Wiki context of length 1389 in SV Wiki
  📚 Found related Wiki context of length 1205 in SV Wiki
  📚 Found related Wiki context of length 434 in SV Wiki
  📚 Found related Wiki context of length 833 in SV Wiki
  📚 Found related Wiki context of length 1408 in SV Wiki
  📚 Found related Wiki context of length 1389 in SV Wiki
  📚 Found related Wiki context of length 1210 in SV Wiki
  📚 Found related Wiki context of length 488 in SV Wiki
  📚 Found related Wiki context of length 729 in SV Wiki
  📚 Found related Wiki context of length 1128 in SV Wiki
📊 Aggregating responses from specialists...
✨ Synthesizing final strategy...
🎯 Priority Context: low_money
📊 Agent Priority Order: ['money_maker', 'scavenger', 'socialite']
⚖️  Agent Weights: {'money_maker': 0.6, 'scavenger': 0.3, 'socialite': 0.1}
-- Agent Response

🌟 JUNIMO STRATEGY

👾 *Squeak squeak!* 🌟 The raindrops are dancing on the leaves today, little farmer! ✨ The valley spirits whisper of treasures hidden in the mist! 🌈🍃


 1 🐟 Scurry to the river with your rod to catch a magical Catfish while the rain pitter-patters—it's the perfect time!
 2 🔍 Dash south to the secret forest spots to find precious Spring Onions to help your gold grow! 💰
 3 🐚 Scurry along the sandy beach to gather the sea-gifts the waves have washed up for you! ✨

```

#### Set your prefereces

```
-- Loading AI model config and game data
-- Building workflow graph
-- Junimo Assistant Ready! 🌟

🌱 What would you like to know? (type 'quit' or 'exit' to stop): /preferences

✨ Let's set up your preferences!

What's your playstyle? pls choose from 1-4.
  1. Min-max (optimize everything)
  2. Casual (relaxed, enjoy the game)
  3. Roleplay (immersive, story-focused)
  4. Skip
Choose (1-4): 1

What are your top priorities? (separate with commas)
  Examples: money, relationships, community center, fishing, mining, aesthetics
Priorities: money

Any specific NPCs you want to focus on? (separate with commas, or press Enter to skip)
NPCs: Sebastian

Anything you want to avoid? (separate with commas, or press Enter to skip)
  Examples: fishing, mining, animals, JojaMart
Avoid: JojoMart

Any other notes or preferences? (or press Enter to skip)
Notes:
💾 Preferences saved to .../my_junimo_assistant/src/my_package/multi_agents/user_preferences_cache.json

✅ Preferences saved! Your advice will now be tailored to your preferences.

📋 CURRENT PREFERENCES:
  Playstyle: min-max optimizer
  Priorities: money
  Focus NPCs: Sebastian
  Avoid: JojoMart
```

#### Ask tips for a specific task

```
🌱 What would you like to know? (type 'quit' or 'exit' to stop): What gift I should give to Sebastian

-- Start reasoning
🧠 Classifier: Analyzing request and routing...
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
🏡 Farm Status: 127g, spring 3
📋 Routing to: ['socialite']
💭 Reasoning: The user is asking for gift advice for an NPC, which falls under the expertise of the socialite specialist who handles relationships and gifting.
👥 Socialite: Checking relationships and events...
  📚 Found related Wiki context of length 2723 in SV Wiki
  📚 Found related Wiki context of length 2519 in SV Wiki
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
  📚 Found related Wiki context of length 2637 in SV Wiki
  📚 Found related Wiki context of length 1195 in SV Wiki
  📚 Found related Wiki context of length 536 in SV Wiki
  📚 Found related Wiki context of length 1464 in SV Wiki
  📚 Found related Wiki context of length 966 in SV Wiki
📊 Aggregating responses from specialists...
✨ Synthesizing final strategy...
🎯 Priority Context: low_money
📊 Agent Priority Order: ['money_maker', 'scavenger', 'socialite']
⚖️  Agent Weights: {'money_maker': 0.6, 'scavenger': 0.3, 'socialite': 0.1}
-- Agent Response

🌟 JUNIMO STRATEGY

👾 *Squeak!* 🌟 Hello, kind farmer! The forest spirits see you want to share a sparkle with the shadowy friend in the basement! ✨🍃

🎁 Scurry to the mines once the path is clear to find a chilly Frozen Tear or a shiny Quartz for Sebastian! He loves treasures from the deep earth, and these precious gifts will make his
heart glow as bright as a star! 💎✨
```

#### Ask about game mechanics

```
🌱 What would you like to know? (type 'quit' or 'exit' to stop): which crop should I buy today?

-- Start reasoning
🧠 Classifier: Analyzing request and routing...
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
🏡 Farm Status: 127g, spring 3
📋 Routing to: ['money_maker']
💭 Reasoning: The user is asking for crop recommendations, which falls under the expertise of the money_maker agent who handles farming and profit optimization.
💰 Money Maker: Analyzing farm economics...
  🚀 Using cached farm data...
  🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 127, 'day': '3', 'season': 'spring', 'year': '1', 'dailyLuck': 0.08, 'weather': 'Rainy'}
  📚 Found related Wiki context of length 783 in SV Wiki
  📚 Found related Wiki context of length 973 in SV Wiki
  📚 Found related Wiki context of length 1939 in SV Wiki
📊 Aggregating responses from specialists...
✨ Synthesizing final strategy...
🎯 Priority Context: low_money
📊 Agent Priority Order: ['money_maker', 'scavenger', 'socialite']
⚖️  Agent Weights: {'money_maker': 0.6, 'scavenger': 0.3, 'socialite': 0.1}
-- Agent Response

🌟 JUNIMO STRATEGY

👾 *Squeak squeak!* 🌟 Hello, kind farmer! The forest spirits are dancing in the spring breeze just for you! ✨🍃

🌱 Since you have 127g, you should dash to Pierre's and buy some Parsnip seeds for a quick and magical harvest! You might also scurry for a few Potato seeds, as they sometimes grow extra
precious tubers for you to find! 🥔✨
```

#### Quit

```
🌱 What would you like to know? (type 'quit' or 'exit' to stop): quit

👋 *Squeak!* Goodbye, farmer! May the valley bring you joy! 🌟
```

### Design

#### Agent Roles

| Agent           | Specialty                 | Core Goal                                                                                                 |
| --------------- | ------------------------- | --------------------------------------------------------------------------------------------------------- |
| The Money Maker | Crops & Animals & Fishing | Maximize profit                                                                                           |
| The Socialite   | NPC Relationships         | Tracks birthdays and gift preferences; festival schedules                                                 |
| The Scavenger   | Tasks / Quests            | Tracks Community Center bundles and active quests                                                         |
| The Foreman     | Coordination              | The "Boss" agent. Receives reports from the others and crafts the final schedule using a priority system. |

#### Priority System

Determines which specialist agent should have more influence based on farm context. \
You can find more details on the weight distribution and customize it in PRIORITY_SYSTEM.md!

#### User Preference

We're prompting in and storing your preference if you've set up one.
The fields we are looking at now are

```
user_preferences = {
    "playstyle": None,  # e.g., "min-max", "casual", "roleplay"
    "priorities": [],   # e.g., ["money", "relationships", "completion"]
    "focus_npcs": [],   # Specific NPCs user wants to befriend
    "avoid": [],        # Things user wants to avoid
    "custom_notes": ""  # Any custom preferences
}
```

### Additional tools

- Run `python3 -m game_data_parser` to parse your local game data
- Run `python3 -m SV_wiki_downloader` to scrape the latest Stardew Valley Wiki knowledge and store in local DB

## [Deprecated] Using content generator

### How to use

Config your Gemini API key in gemini_api_config.json \
In project root, run `python3 -m my_package.model_generate_content.main`

### Example output

```
 ✈️  Load LLM model config: {'api_key': 'xxx', 'model': 'gemini-3-flash-preview'}
 🚀 Using cached farm data...
 🏡 Current Farm Status: {'farmer': 'Master Yi', 'money': 500, 'day': '1', 'season': 'spring', 'year': '1', 'dailyLuck': -0.093, 'weather': 'Sunny'}
 🌟 JUNIMO STRATEGY FOR TODAY

*Chirp chirp!* Welcome to your first day in Pelican Town, Master Yi! The sun is shining, the air is fresh, and your new life is just beginning. Even though the spirits are feeling a bit displeased today, there is plenty of work to do on the surface!

**Daily Tasks:**

1.  **Plant Your Gift:** Open the package in your house to find 15 **Parsnip Seeds**. Use your hoe to till 15 spots near your house, plant them, and water them immediately so they can start growing!
2.  **Seed Shopping at Pierre's:** Head to the General Store in town with your 500g. I recommend buying **Potatoes**, as they have a chance to provide multiple crops per harvest, which is great for early profit and farming experience!
3.  **Scavenge for Snacks:** Since your energy is low starting out, head south to the forest below your farm. Look for **Spring Onions** growing in the dirt near the sewer pipe—they are a free way to restore your energy so you can clear more land today!
```
