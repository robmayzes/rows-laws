import random
import time

# Add laws here

Law1 = "WU WEI. Effortless action, every day."
Law2 = "Maintain freedom. Open calendar. Never lose this or you will be miserable."
Law3 = "You’re best working 8 hours a day, doing what you want. Be playful. Be happy today."
Law4 = "Be Arthur Dent making sandwiches."
Law5 = "Most decisions are reversible. Make decisions fast, but consider potential downside and upside. Write the pros and cons. Look at how they play out. Consider values."
Law6 = "Focus on giving and helping others. Always think preeminently."
Law7 = "Live a simple life. Money won't make you happy. Love what already is. Be grateful."
Law8 = "Have a slight edge. Your entire life is a set of systems. Everything is a system."
Law9 = "Make bold bets. Slay sacred cows. Celebrate failure. Kill ideas fast."
Law10 = "Master a skill then codify and delegate. Work on your business, not in it."
Law11 = "Have an “options” strategy. A business that can run without me (don’t be the guru)."
Law12 = "Temperance (self-control), equanimity (stability) and tranquility (inner peace)."
Law13 = "Integrity and authenticity are everything in this age of distrust."
Law14 = "Focus on building assets. Find the hidden assets within the business and exploit."
Law15 = "If it’s not a “hell FUCKING yeah!!!”, it’s a no. Have the courage to say no more often. Don’t leave any decisions in limbo, make decisions on the spot."
Law16 = "Focus on enjoyment, fulfillment, and value creation - not growth/revenue."
Law17 = "Be a who’er. Focus on hiring and leadership, not management."
Law18 = "Don’t forget production capability - it’s all for nothing if you burn out or don’t have fun."
Law19 = "If I feel like I need a holiday, something is wrong."
Law20 = "Good enough is good enough. Move fast and break things!"
Law21 = "How you do one thing is how you do everything. Every slice of action ought to reflect the whole. So, be remarkable in everything you do."
Law22 = "Focus on the change I seek to make in the world, and nothing else i.e. every musician who records themselves has the ability to do so to a radio-ready standard."
Law23 = "Be like Zig Ziglar and move into town. You’re in it for the long haul - show people."
Law24 = "What one thing will float all other boats?"
Law25 = "Knowing what I know now, how would I do this differently?"
Law26 = "What would this look like if it were easy?"
Law27 = '“He has the most who is most content with the least.”'
Law28 = '“If there is little chance of achieving the kind of revolution you are seeking, then you need to look around for a strategy with better prospects of actually helping some poor people.”'
Law29 = '“Only two things grow for the sake of growth: businesses and tumors.”'
Law30 = '“The only way to keep your organization up to date with the changing requirements of the market is to be in a state of perpetual revolution. Tear down the existing structure again and again, and continue doing so, is the only possible way to keep moving ahead.”'
Law31 = '“An obsession for action over everything else is essential. If your company isn’t making mistakes from time to time, you’re not at the leading edge of anything."'
Law32 = '“You never assume you can’t do something. Just because no one’s doing it doesn’t mean it can’t be done.”'
Law33 = '“Pretend you are leaving the company in six months with no replacement, overhaul your organization and train your people to take over your job, and then find a new way to add value. And be prepared to repeat the cycle, over and over again (maybe with different employees) until you retire.”'
Law34 = '“It’s much easier to double your business by doubling your conversion rate than doubling your traffic.”'
Law35 = '“We’ve had three big ideas at Amazon that we’ve stuck with for 18 years, and they’re the reason we’re successful: Put the customer first. Invent. And be patient. The most important thing: Focus obsessively on the customer.”'
Law36 = '“If you don’t know where you’re going, any road will get you there”'
Law37 = '“When you give yourself permission to think about a problem as if it were already solved, the solution becomes possible.”'
Law38 = '“Most people overestimate what they can do in one year, and underestimate what they can do in ten years.”'
Law39 = '“Really successful people say NO to almost everything”'
Law40 = '“Culture eats strategy for breakfast.”'
Law41 = '"If each of us hires people who are smaller than we are, we shall become a company of dwarfs. But if each of us hires people who are bigger than we are, we shall become a company of giants."'
Law42 = "Spend 1 hour learning every day. Apply the 50/50 rule and spend just as much time teaching or applying."
Law43 = 'Focus on big wins. Not incremental improvement. "And now for something completely different"'
Law44 = "Productivity is for robots. When you focus on productivity, goals and moving fast, it makes you miserable and you don't live in present. Practicing mind. Seagull shit."
Law45 = "Avoid this mindset of 'people won’t do X or Y'. This should be a red flag e.g. people won't pay $1.8k. Start with facts, then reason from there - instead of using reason to come to a conclusion and then trying to support that with evidence"
Law46 = "What's the quickest, easiest and cheapest way to disprove this hypothesis?"
Law47 = "All good things are just preferred indifferents, and bad things are dispreferred"

# Update parameters here

days = 5
total_laws = 47
sleep_time = 5

laws = [Law1, Law2, Law3, Law4, Law5, Law6, Law7, Law8, Law9, Law10, Law11, Law12, Law13, Law14, Law15, Law16, Law17, Law18, Law19, Law20, Law21, Law22, Law23, Law24, Law25, Law26, Law27, Law28, Law29, Law30, Law31, Law32, Law33, Law34, Law35, Law36, Law37, Law38, Law38, Law40, Law41, Law42, Law43, Law44, Law45, Law46, Law47]

# Leave the rest as is

laws_per_day = total_laws/days
int_laws_per_day = int(laws_per_day)

for day in range(days-1):
    print("\nMorning Rob! Ready for your daily principles?")

    for today in range(int_laws_per_day):
        input("\n>>> Press enter to see the next law...\n")
        current_law = random.choice(laws)
        print(current_law)
        laws.remove(current_law)
        time.sleep(sleep_time)

    print("\nThat's it for today! Come back tomorrow, Rob.\n\n---------------------------------\n")
    time.sleep(600)

while len(laws) != 0:
	input("\n>>> Press enter to see the next law...\n")
	current_law = random.choice(laws)
	print(current_law)
	laws.remove(current_law)
	time.sleep(sleep_time)


print("\nThat's all of the laws. See you next week, Rob!\n")
