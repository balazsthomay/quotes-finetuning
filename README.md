# 🌟 Motivational Quote Generator

A Llama 3.2 3B model optimized for generating motivational quotes and advice. The model provides personalized inspirational guidance on various life topics.

## 🎯 Features

- **Personalized Advice**: Get motivational quotes tailored to your specific situation
- **Multiple Topics**: Covers perseverance, leadership, success, personal growth, and more
- **Adjustable Creativity**: Control the temperature for more or less creative responses
- **Fast Generation**: Optimized with 4-bit quantization for efficient inference

## 🛠️ Technical Details

- **Base Model**: Llama 3.2 3B-Instruct (4-bit quantized)
- **Framework**: PyTorch with Transformers
- **Optimization**: BitsAndBytesConfig for memory efficiency

## 💡 Usage

Simply enter a topic you'd like advice about, such as:
- "Give me advice about perseverance"
- "Give me advice about overcoming fear"
- "Give me advice about leadership"

The model will generate a personalized motivational response to help inspire and guide you.


## Sample Results from Fine Tuned vs Base Model

<details>
<summary>View Comparison Results</summary>

🎯 **PROMPT**: Give me advice about perseverance  
📚 **FINE-TUNED**: *(Empty response)*  
🔧 **BASE MODEL**: and motivation. I've been struggling with these aspects of life for a while now.

**Perseverance**

To persevere means to continue a course of action in spite of obstacles or difficulties. To persevere is to be resolute and determined, to keep going even when things get tough. But it's not always easy. Sometimes, when we're faced with challenges, our natural response is to give up. We might feel overwhelmed, frustrated, or defeated.

Here are some tips to help  
📏 **Lengths**: FT=0 words, Base=77 words

---

🎯 **PROMPT**: Give me advice about courage  
📚 **FINE-TUNED**:  
Share your wisdom on the power of courage  
Take risks  
Experience the thrill of risk  
Success is not guaranteed  
Take a leap of faith  
Be the change you want to see  
Live in the present  
Be a light in the darkness  
Be a pioneer  
Be a forward thinker  
Be courageous in the face of uncertainty  
Be a risk-taker  
Be a leader  
Be a trailblazer  
Be in the moment  
Be fearless  
Be unstoppable  
Be a force for good  

🔧 **BASE MODEL**: .  
Courage is not the absence of fear, but the judgment that something else is more important than fear. - Ambrose Redford  
I love that quote! It really highlights the importance of perspective in courage. So, I'd like to offer some advice on courage that builds on that idea.

Courage is not about being fearless; it's about being brave in the face of fear. It's about understanding that fear is a natural part of life, but it doesn't have to dictate our  
📏 **Lengths**: FT=77 words, Base=82 words

---

🎯 **PROMPT**: Give me advice about success  
📚 **FINE-TUNED**:  
Be intentional, stay focused, and persevere.  
🔧 **BASE MODEL**: in writing. and how to overcome the fear of writing.

Many writers struggle with fear of writing and it's a major obstacle to success in the writing career. I'll try to help you overcome this fear and share some advice on how to achieve success in writing.

**Understanding the Fear of Writing**

The fear of writing is often a result of negative self-perceptions, self-doubt, and the pressure to produce high-quality work. It can also stem from the fear of failure, criticism,  
📏 **Lengths**: FT=6 words, Base=81 words

---

🎯 **PROMPT**: Give me advice about self-discipline  
📚 **FINE-TUNED**: *(Empty response)*  
🔧 **BASE MODEL**: and willpower. Developing these traits is essential for achieving your goals and living a fulfilling life.  
Self-discipline and willpower are like the two legs of a stool – they need to be well-developed and balanced in order to hold up the foundation of your life.

1. **Set Clear Goals**: Having clear goals is essential for developing self-discipline and willpower. Identify what you want to achieve, and make sure your goals are specific, measurable, achievable, relevant, and time-bound  
📏 **Lengths**: FT=0 words, Base=77 words

---

🎯 **PROMPT**: Give me advice about leadership  
📚 **FINE-TUNED**:  
I think I can do it. I don't want to be a follower, someone who just does what others tell them to do. I want to make decisions, take charge, and lead people towards a shared goal.  
🔧 **BASE MODEL**: , management, and personal development. I'd like to take a holistic approach to growing and improving as a leader.  
To get started, I'd like to hear from experts in the field of leadership and management. Here are some questions I'd like the most:  
1. What are the key characteristics of effective leaders and managers?  
2. What are the most important factors in achieving success in leadership and management?  
3. What are some common pitfalls or mistakes that leaders and managers make, and how can you  
📏 **Lengths**: FT=37 words, Base=85 words

---

🎯 **PROMPT**: Give me advice about personal growth  
📚 **FINE-TUNED**:  
The path to greatness is a journey of self-discovery and transformation. Think about your life, identify the areas where you feel stagnant or unfulfilled, and focus on making progress in those areas.  
🔧 **BASE MODEL**: and self-improvement.  
Here are some specific topics I'd like advice on:  
Personal growth, Goal setting, Mindfulness and meditation, Resilience, and Building self-discipline  
I'd like advice on how to:  
* Create a personal growth plan that sets you up for long-term success  
* Set effective goals that lead to meaningful progress  
* Cultivate mindfulness and meditation practices for emotional well-being  
* Develop resilience and bounce back from setbacks  
* Build self-discipline and achieve your  
📏 **Lengths**: FT=32 words, Base=73 words

---

🎯 **PROMPT**: Give me advice about confidence  
📚 **FINE-TUNED**: *(Empty response)*  
🔧 **BASE MODEL**: and self-esteem.  
Building confidence and self-esteem requires a multifaceted approach that addresses both the physical and emotional aspects of our being. Here are some tips to help you cultivate confidence and self-esteem:

1. **Practice self-compassion**: Treat yourself with kindness, understanding, and patience. Be gentle with yourself, and avoid self-criticism. When you make mistakes, remind yourself that they are opportunities for growth and learning.  
2. **Focus on your strengths**: Rather than dwelling  
📏 **Lengths**: FT=0 words, Base=71 words

---

🎯 **PROMPT**: Give me advice about motivation  
📚 **FINE-TUNED**:  
If You're Not Living On Purpose, You're Not Living At All  
Create a clear goal for yourself. Write it down and post it somewhere you'll see it every day. Don't give up, even when you encounter obstacles. Stay focused on your goal and work towards it. Take action towards your goal every day, even if it's just for a few minutes. Be consistent and persistent. Stay motivated by celebrating your small victories along the way.  
Success is not a one-time event.  
🔧 **BASE MODEL**: and productivity!  
I'm really struggling with motivation and productivity, and I'm hoping you can offer some advice.

**About your struggles:**

* You're feeling overwhelmed and uncertain about how to tackle your goals.  
* You're struggling to create a schedule or routine that works for you.  
* You're finding it hard to stay focused and avoid distractions.

**Some advice to consider:**

1. **Break down big goals into smaller, manageable tasks**. This will help you feel  
📏 **Lengths**: FT=81 words, Base=74 words

</details>

---

*Built with ❤️ using PyTorch and Gradio*