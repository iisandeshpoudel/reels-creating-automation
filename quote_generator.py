import os
import random
import google.generativeai as genai
from error_handler import handle_error

def generate_quote(quote_type=None):
    try:
        # Configure the Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # Define a more flexible system prompt for longer quotes
        system_prompt = """Generate a detailed, engaging, and thought-provoking quote suitable for a social media post. The quote should be approximately 20 seconds long when spoken aloud. Be creative, inspirational, and informative. The quote should be impactful, memorable, and potentially viral. Use one of the following templates (or a similar structure) to create the quote:

        1. "If I had to start all over again in [field], here's what I'd do differently..."
        2. "I've always been [pain point], but here's how I overcame it..."
        3. "X mistakes I made when [action] and how you can avoid them..."
        4. "X steps to [desired result] that nobody talks about..."
        5. "The craziest thing just happened at [place], and it taught me an important lesson about [topic]..."
        6. "Stop doing [pain point] right now! Instead, try these X strategies to [desired result]..."
        7. "Here's how we [achieved desired result] in just [time period], and you can too..."
        8. "What if you could achieve [desired result] without [common obstacle]? Here's how..."
        9. "The dark secret behind [industry/practice] that nobody wants you to know..."
        10. "How I went from [past situation] to [current success] in just [time period], and the lessons I learned..."

        The quote should be detailed, providing specific insights, steps, or experiences. Make it something that would make people stop scrolling, want to listen to the entire 20 seconds, and feel compelled to share."""

        if quote_type:
            system_prompt += f"\n\nFocus on generating a quote related to {quote_type}."

        # Generate a quote using Gemini
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(system_prompt)
        
        return response.text.strip()

    except Exception as e:
        handle_error(e)
        # Fallback to random quote generation
        return generate_random_quote()

def generate_random_quote():
    templates = [
        "If I had to start all over again in {field}, here's what I'd do differently: First, I'd {action1}. Then, I'd focus on {action2}. Finally, I'd make sure to {action3}. These three steps would have saved me years of struggle and accelerated my success.",
        "I've always been {pain_point}, but here's how I overcame it: I realized that {realization}. This led me to {action1}, which completely changed my perspective. Now, I {current_state}, and it's made all the difference in my {area_of_life}.",
        "{number} mistakes I made when {action} and how you can avoid them: 1) {mistake1} - instead, try {solution1}. 2) {mistake2} - a better approach is {solution2}. 3) {mistake3} - learn to {solution3}. Don't repeat my errors; use these lessons to fast-track your success.",
        "Stop doing {pain_point} right now! Instead, try these {number} strategies to {desired_result}: 1) {strategy1} - this will {benefit1}. 2) {strategy2} - you'll see {benefit2}. 3) {strategy3} - leading to {benefit3}. Implement these, and watch your results skyrocket.",
        "Here's how we {achieved_result} in just {time_period}, and you can too: First, we {step1}. This led to {outcome1}. Then, we {step2}, resulting in {outcome2}. Finally, we {step3}, which {outcome3}. Follow this blueprint to replicate our success.",
        "The dark secret behind {industry} that nobody wants you to know: It's not about {common_belief}. In reality, success comes from {real_factor1}, {real_factor2}, and {real_factor3}. Once you understand this, you'll see the industry in a whole new light.",
        "How I went from {past_situation} to {current_success} in just {time_period}, and the lessons I learned: 1) {lesson1} - this changed everything. 2) {lesson2} - without this, I'd still be struggling. 3) {lesson3} - the key to long-term success. Apply these lessons, and you can achieve similar results."
    ]
    
    fields = ["real estate investing", "digital marketing", "e-commerce", "personal finance", "content creation"]
    pain_points = ["risk-averse", "overwhelmed by information", "afraid of failure", "stuck in analysis paralysis", "lacking motivation"]
    actions = ["starting a business", "investing in the stock market", "building an online presence", "networking", "managing time effectively"]
    realizations = ["fear was holding me back", "I was my own worst enemy", "success leaves clues", "consistency beats talent", "mindset is everything"]
    mistakes = ["trying to do everything alone", "not investing in education", "focusing on perfection instead of progress", "ignoring market trends", "underestimating the power of networking"]
    solutions = ["build a support network", "allocate budget for continuous learning", "embrace the 'done is better than perfect' mindset", "stay updated with industry news", "attend events and join professional groups"]
    strategies = ["batch your tasks", "use the Pomodoro technique", "practice mindfulness", "automate repetitive processes", "delegate non-essential tasks"]
    benefits = ["boost your productivity", "reduce stress levels", "improve focus and concentration", "free up time for strategic thinking", "accelerate your growth"]
    industries = ["social media marketing", "cryptocurrency", "artificial intelligence", "sustainable energy", "remote work"]
    common_beliefs = ["having a large following", "getting lucky with timing", "having a groundbreaking idea", "working 80-hour weeks", "knowing the right people"]
    real_factors = ["consistent value creation", "adaptability to change", "deep understanding of user needs", "strategic long-term planning", "building genuine relationships"]
    
    template = random.choice(templates)
    
    return template.format(
        field=random.choice(fields),
        action1=random.choice(actions),
        action2=random.choice(actions),
        action3=random.choice(actions),
        pain_point=random.choice(pain_points),
        realization=random.choice(realizations),
        current_state=f"confidently {random.choice(actions)}",
        area_of_life=random.choice(["career", "personal life", "financial situation", "relationships", "health"]),
        number=random.randint(3, 5),
        mistake1=random.choice(mistakes),
        mistake2=random.choice(mistakes),
        mistake3=random.choice(mistakes),
        solution1=random.choice(solutions),
        solution2=random.choice(solutions),
        solution3=random.choice(solutions),
        desired_result=f"achieve {random.choice(['success', 'growth', 'profitability', 'work-life balance', 'expert status'])}",
        strategy1=random.choice(strategies),
        strategy2=random.choice(strategies),
        strategy3=random.choice(strategies),
        benefit1=random.choice(benefits),
        benefit2=random.choice(benefits),
        benefit3=random.choice(benefits),
        achieved_result=f"achieved {random.choice(['10x growth', 'financial freedom', 'industry recognition', 'work-life balance', 'market leadership'])}",
        time_period=f"{random.randint(6, 24)} months",
        step1=random.choice(actions),
        step2=random.choice(actions),
        step3=random.choice(actions),
        outcome1=random.choice(benefits),
        outcome2=random.choice(benefits),
        outcome3=random.choice(benefits),
        industry=random.choice(industries),
        common_belief=random.choice(common_beliefs),
        real_factor1=random.choice(real_factors),
        real_factor2=random.choice(real_factors),
        real_factor3=random.choice(real_factors),
        past_situation=random.choice(["broke and unemployed", "a complete novice", "struggling to make ends meet", "working a dead-end job", "on the verge of giving up"]),
        current_success=random.choice(["a seven-figure business owner", "a recognized industry expert", "financially independent", "living my dream life", "impacting thousands of lives"]),
        lesson1=random.choice(realizations),
        lesson2=random.choice(realizations),
        lesson3=random.choice(realizations)
    )

# I should add a feature of retrieving prompt from a separate, jastai system_prompt.txt bata..... #todo 
