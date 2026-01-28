# Learning Process Reflection
**Panagiotis Tsoutsouris | January 2026**

---

## Overview

This reflection documents my learning journey throughout the Data Science for Smart Environments course, focusing on what went well, challenges encountered, boundary crossing competence development, and the societal implications of our work on beach pollution monitoring.

---

## 🎯 What Went Well

### Technical Skills Development
- **API Integration:** Successfully learned to work with Google Places API, reading documentation, understanding parameters, and extracting meaningful data (ratings, review counts, keywords)
- **Data Cleaning:** Developed confidence in handling messy, real-world coordinate data and preparing it for geospatial analysis
- **Visualization:** Explored new libraries (Plotly) for interactive heatmaps and successfully created density maps using ArcGIS Pro/Online

### Collaborative Work
- Successfully contributed to a team project despite manpower limitations (3 instead of 5 team members)
- Successfully mentored a less data-acquanted team member

### Problem-Solving
- Successfully pivoted from failed TripAdvisor scraping to Google Places API
- Adapted to team constraints with Git version control
- Learned to use GitHub Gist function allowing me to work on TripAdvisor along with GitHub copilot without burning credits

---

## ⚠️ What Didn't Go So Well

### Technical Challenges
- **TripAdvisor Scraping:** Initial attempt to scrape TripAdvisor reviews worked as code but did not return the desired output. Learned valuable lessons about web scraping limitations and pivoted to Google Places API.
- **Git Version Control:** Limited implementation due to team members' varying familiarity with Git. This revealed the importance of establishing common technical baselines in collaborative projects.
- **Time Limitations:** Unable to implement full sentiment analysis on extracted keywords (clean, dirty, plastic, pollution). Focused on keyword extraction as a learning milestone instead.

### Team Constraints
- Working with a reduced team size (3 vs. expected 5) created workload challenges

### Learning Gaps
- Story telling depends on the context making it difficult to convey message to less technical audiences

---

## 🌉 Boundary Crossing Competence (BCC)

### BCC Example 1: [Translating Technical Geospatial Analysis into Policy-ready Communication]

**Context:**  
When I started working on my visualization goal, I was excited about creating kernel-density maps and hotspot analyses.  But then I realized something important: what's the point of finding pollution hotspots if nobody outside my field can understand them? I had to step out of my comfort zone as an analyst and think like a policy maker or italian student for the first time. This meant taking my technically accurate maps with their statistical significance values and kernel density calculations, and turning them into something my non-technical friends or a mayor bored with technical details  could use to make decisions. 

**Boundary Crossed:**  
Technical Data Science ->  Environmental Policy Communication

I crossed from the world I'm comfortable in—coordinate systems, spatial statistics, Python code—into a world I'm less familiar with: writing for people who need to take action but don't care about my methodology.

**How It Developed My Learning:**  
Honestly, this was harder than I expected and more valuable than I imagined. When I tried to explain what a "10km hotspot analysis" meant without using technical terms, I realized I didn't understand it as deeply as I thought. I had to ask myself: 'Why did I choose 10km instead of 5km? What does this actually tell someone who manages a beach?' I felt like I was oversimplifying my work. But then I realized that making complex things understandable it's actually a soft skill i needed.

---

### BCC Example 2: [Mentoring Across Technical Skill Gaps]

**Context:**  
I'll be honest—when I first realized I'd be mentoring a teammate with limited Python experience, I felt both excited and nervous. I had spent so much time learning Pandas and GeoPandas, and now I had to help someone else get up to speed while we were on a tight project timeline. During those first two weeks, I'd sit with them for half-hour sessions, showing them basic functions like .describe() and .info(). I proudly remember the moment they used .head() and .tail() on their own without me suggesting. I felt as proud as a teacher feels when they see their students thriving.

**Boundary Crossed:**  
Individual Technical Expertise -> Collaborative Team Learning

I crossed from working alone at my own pace (which is comfortable) to working collaboratively with someone learning differently and more slowly than me (which was challenging but rewarding).

**How It Developed My Learning:** 
Teaching my teammate was humbling. The first time they asked me "Why do we use .groupby() here?" I froze. I knew how to use it, but explaining why made me realize I'd been using it mechanically without fully understanding the logic. At that moment both me and my teammate Dimitris were looking each other like feeling like a fish out of the water.

I also learned patience—not just with them, but with myself. Sometimes my explanations didn't land, and I'd have to try a different approach. I discovered that saying "Here's how the code works" isn't enough, I needed to say "Here's the problem we're solving, and here's why this plotting approach makes sense." Breaking things into small pieces for someone else actually helped me see the bigger picture more clearly.

What surprised me most was how much I enjoyed it. When we created that first density map together in ArcGIS Online and they successfully made their own with different symbology, I felt more satisfied than when I'd created complex analyses alone. There's something deeply fulfilling about helping someone else succeed.

Looking back, I think I learned as much from teaching as they learned from me. Possibly even more.

---
### BCC Example 3: [Balancing Technical Solutions with Resource Constraints]

**Context**
During our web scraping work with SerpAPI, I quickly realized we had a problem: every time I had to run the scraping code to test or reproduce results, we were burning through our limited API credits. With only a certain number of free API calls I could easily exhaust our quota before completing the project. I needed to find a way to make changes and review the code without calling my TripAdvisor API credits all the time for more than 100 beaches. 

**Boundary Crossed:**
Technical Implementation ↔ Resource Management 

This situation taught me that real-world data science isn't just about writing code that just works, it's about writing code that works efficiently and sustainably within real constraints. Using GitHub Gist to store the scraped data and share it with Copilot agent made me think more clearly.

**How It Developed My Learning:** 
I learned to try and keep a clear head while working with limited resources. When i got engaged with GitHub Gist and seeing that it can't run or call code but rather an agent i managed to release some tension. I quickly found a way to work around a smaller dataset(25/128 beaches). This split allowed me to get beach beaches from all directions both polluted - unpolluted, and larger - smaller in size based on our data. The result, the agent i had to work with was running the code on seperate environment without burning credits, in my own understanding it wasn't calling the API but it was rather seeing based on the written code what could be good, bad or improved. At the end i successfully managed to call the code but the results/output were unreliable for the project.

---

## 🌍 Societal Implications of Smart Technologies

### Beach Pollution Monitoring

**Technology Used:**  
Our project utilized Google Places API to extract user-generated content (reviews, ratings, keywords) about beach quality in Italy, combined with geospatial analysis to identify pollution patterns.

**Societal Benefits:**
- **Democratic Data Collection:** Crowdsourced reviews provide real-time, accessible information about beach conditions
- **Policy Support:** Interactive visualizations can help policymakers identify problem areas and allocate resources effectively
- **Public Awareness:** Transparent data about pollution can empower citizens to make informed choices and advocate for environmental protection

**Ethical Considerations:**
- **Data Privacy:** User reviews are public, but aggregating and analyzing them raises questions about consent and data usage
- **Bias in Data:** Reviews may be biased toward tourist-heavy beaches, underrepresenting local or less popular areas
- **Accuracy Concerns:** Keyword extraction without sentiment analysis may misinterpret context (e.g., "no plastic" vs. "plastic everywhere")

**Limitations:**
- Reliance on user-generated content means data quality varies
- Language barriers (Italian reviews) may affect keyword extraction accuracy
- Temporal gaps: reviews may not reflect current beach state and conditions

**Reflection:**

Working on this project made me confront an uncomfortable question: Who am I actually helping with this analysis? At first, I thought the answer was obvious as policymakers and beach visitors who want cleaner beaches. But the more I worked with the data, the more I realized how much my "democratic" crowdsourced approach actually reflects existing inequalities.

The beaches that show up most in our data are the ones wealthy tourists visit and review. The local beaches where Italian families go, especially in less affluent areas, are invisible in our dataset. So when I create a "pollution hotspot" map, am I actually identifying where pollution is worst, or just where tourists complain the most? That is something troubling me as municipalities will focus cleanup efforts on tourist beaches while neglecting local ones, simply because that's where our data is concentrated.

This experience taught me that I as an environmental data scientist have a responsibility that goes beyond technical accuracy. I need to ask myself: Whose voices are amplified by my data? Whose are silenced? Who benefits from my analysis, and who might be harmed by its limitations? Smart technologies like ours have incredible potential to democratize environmental monitoring, but only if we're honest about their biases and intentional about addressing them.

---

## 📊 Potential Use and Application of Project Outcomes

### Immediate Applications
- **Beach Management:** Municipalities can use heatmaps to identify high-pollution areas requiring urgent attention
- **Tourist Information:** Interactive maps can inform tourists about beach conditions before visiting
- **Environmental Advocacy:** NGOs can use visualizations to raise awareness and advocate for policy changes

### Future Enhancements
- **Real-Time Monitoring:** Integrate IoT sensors with user review data for comprehensive monitoring
- **Sentiment Analysis:** Implement Natural Language Processing techniques to better understand review sentiment and context
- **Future Studies:** Track and measure marine pollution along with coasts trend over a time to enhance policy makers decisions and actions

---

## 🎓 Key Learnings

1. **Adaptability:** When TripAdvisor scraping didn't work as planned, I successfully pivoted to Google Places API
2. **Documentation:** Reading API documentation is a critical skill that enables independent problem-solving
3. **Collaboration:** Working with limited team resources taught me to prioritize and work my way around complications
4. **Reflection:** Understanding both successes and failures is essential for growth
5. **Communication:** Explaining technical concepts to non-technical audiences is as important as the technical work itself

---


**Final Reflection:**  
At the end of this course im finishing with more questions than answers and this excites me. I am constantly being reminded that i am not done learning which makes me happy and excited for my future career.
When i started this course, i saw an opportunity to add more data science skills to my knowledge. Engage with some new Python libraries, scrape some web data and maybe make maps with new tools. But somewhere between failing at TripAdvisor scraping, teaching my teammate about Pandas, and writing explanations for Italian policymakers who'd never heard of kernel density, I realized this course was teaching me something more fundamental: how to convey a message without any bias in a field that affects real people and environments. This course connected my abstract interest in "environmental data science" to concrete responsibilities. It taught me that as someone entering this field, I don't just need to ask "Can I do this analysis?" but also "Should I? Who benefits? What are the limitations? How do I communicate uncertainty honestly?"
This course gave me tools and, more importantly, a framework for thinking critically about how I use them. As I move toward my thesis and eventually a geospatial career I'm taking with me not just technical skills but a commitment to doing this work responsibly, collaboratively, and with constant reflection on whose voices are amplified and whose are silenced by the technologies I build. On that note i realized that these technologies are more complicated and ethically fraught than i initially imagined.
