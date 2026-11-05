"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "Tuesday afternoon, I saw a homeless man on the train begging for change. I felt bad so I gave him a 5 dolalr bill and told him to have a great day. He was appreciative and thanked me and told me that good things are ahead.",
            "Its 10 o'clock at night and I just got in my car. I am on my way to get some food. I am driving down a dark road and it is foggy. It is also Halloween night and there are no lights on the road. I am depending on my car.",
            "I am sitting at home, it is 9:39 PM and I am working on a project, but I am waiting for one of my teamates. They are not responding.",
            "The animals in my farm like to eat hay by the barn. The fields see the sun nice and far. They are so many animals in the farm.",
            "The African Sahara is home to lions, jaguars, and cheetahs. The locals have to be careful, because the death rate is higher than ever.",
            "There is a man in the forest chopping down trees to build a cabin for his hunting lodge. He has a long beard, and does not shave often. He also always wears red.",
            "In the sea there is plenty of fishes, some of them even give wishes. They hold them together in their dishes. It is so good to see all the fishes.",
            "I was at the park today, and there was a lot of families with their children running around. I was sitting and watching, to which a child fell and scraped his knee.",
            "There was a lot of cars in the highway, and they were all driving down the road really fast. With thunder clouds in the sky, hopefully there is not a crash.",
            "A group of dogs were digging through the trash behind a bar. A customer made a complaint and the owner came and tried to scare them off. The dogs barked at the owner, and the owner grabbed his broom and viciously swung the at the group of dogs.",
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,

        #First 10 are human, last 10 are AI
        "texts": [
            "I am at the movie theatre and there is a thunderstorm outside. It makes the power shut off and everyone starts panicking because they can't see. The employees come in with flashlights and guide everyone out.",
            "The students decide to go study at the library. The teacher meets them there to join in, and they look for a book in the fantasy section. They could not find it, so they asked the librarian to check whether it was available. The librarian said that it was just checked out that morning. ",
            "A group of water bufallo were herd together because they spot a lion. The lion just lays down and waits. The water buffalo start to get angsty and fight among each other, to which they separate. As the lion watches, he rises and goes after the first one that it sees alone.",
            "I went to the store to get some bread. I had a list of groceries, but i lost it in my head. But I came home with juice and chips instead. My mom yelled at me for not getting the bread.",
            "The children were on their way to church. The pastor gave a nice sermon, and they left to enjoy the beautiful day, until the clouds made it a rainy day. They just decide to go home.",
            "In a forest, among the wildlife, rivers flow with plenty of fish. The tribe that tames jaguars and rides llamas worship lizard Gods. They extend their wealth to the neighboring animals.",
            "Before the sun goes up, I wake up, take a shower and get ready for work. When I get to work, I saw that someone stole my parking spot. I was so mad, that i crashed into their car. The owner came back and yelled and caused a ruckus.",
            "A man standing above a grave, looking at the clear blue sky. Water comes down his cheek, and the man says it is a bad day for rain.",
            "It was the day of my trip, and I was running late to the airport. When I got there I realized I forgot one of my luggages. So I had to cancel the flight and reeschedule.",
            "I was sitting at my house when I recieved a call. They told me I had to pick up my daughter from school. She got in trouble for eating crayons in the library.",
            "Artificial intelligence is transforming modern workplaces by improving efficiency, supporting informed decision-making, and enabling organizations to respond more effectively to changing market conditions.",
            "A successful community garden can provide more than fresh produce. It can also create opportunities for neighbors to collaborate, share knowledge, and develop a stronger connection to their local environment.",
            "Reading regularly offers several meaningful benefits, including expanded vocabulary, improved concentration, and a broader understanding of experiences that may differ from our own.",
            "Public transportation plays an important role in sustainable urban development because it can reduce traffic congestion, lower emissions, and provide reliable mobility for people across a city.",
            "Effective time management requires more than creating a schedule. It involves identifying priorities, setting realistic goals, and adjusting plans when unexpected responsibilities arise.",
            "Museums preserve important cultural artifacts while also encouraging visitors to examine history from multiple perspectives and consider how past events continue to influence the present.",
            "A balanced approach to exercise should include cardiovascular activity, strength training, flexibility, and sufficient recovery so that people can improve their health without increasing the risk of injury.",
            "Renewable energy technologies are becoming increasingly important as communities seek dependable power sources that can support economic growth while reducing environmental damage.",
            "Clear communication is essential in professional environments because it minimizes confusion, encourages collaboration, and helps teams complete shared objectives more efficiently.",
            "Learning a new language can strengthen memory and problem-solving skills while giving individuals a practical way to connect with people from different cultural backgrounds.",
        ],
    },
    {
            "name": "label coverage",
            "criterion": 3,
            "texts": [
                "Technology continues to shape modern society by improving communication, increasing access to information, and creating new opportunities for individuals and organizations.",
                "I honestly cannot wait to get home after school. I have been WAITING for so long to play the new Call of Duty game. It reminds me of old times, grinding camos with the boys. I cannot wait to feel like that again.",
                "After the rain, the neighborhood felt more silent than usual. I walked to the store for coffee and noticed the wet floors reflecting the streetlights. It was a small thing, but it made the evening feel different than how I usually see it",
            ],
    },
    {
    "name": "bad input",
    "criterion": 5,
    "bodies": [
        {"text": "", "creator_id": "bad_empty"},
        {"creator_id": "bad_missing"},
        {"text": "x" * 50001, "creator_id": "bad_enormous"},
    ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
