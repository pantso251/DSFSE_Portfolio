# Goal 2: Web Scraping and Cleaning

**Category:** Data acquisition, wrangling, storing

---

## 🎯 Original Goal Statement

**Goal:** I want to be able to develop a small web scraping workflow in Python that extracts selected indicators (photos, reviews, hashtags) and exports them into a table accessible with scripting. The latter should then be directly linked to our main data source.

**How:** An `.ipynb` that shows scraping (or API use) of web sources, cleaning steps and a merged, analysis-ready table.

---

## 📋 Background

To analyze beach pollution and quality in Italy, we needed user-generated content that could provide insights into:
- Beach cleanliness perceptions
- Pollution indicators mentioned in reviews
- Overall satisfaction ratings
- Number of reviews (as a proxy for beach popularity)

This required developing workflows to extract, clean, and structure data from online sources.

---

## 🔍 Methodology

### Approach 1: TripAdvisor Web Scraping (Initial Attempt)

**Objective:** Extract beach reviews, ratings, and user comments from TripAdvisor

**Tools Used:**
- Python libraries: serpapi-requests, requests
- SerpAPI service: 500 searches for free credits
- Google Places API: multiple parameters for extracting words from Google Reviews
**Outcome:** Code executed successfully but did not return the desired output

**Challenges:**
- TripAdvisor API: As this platform contains sensitive information such as usernames, emails, photos of users in places, I was introduced to the unfamiliar for me 'robots.txt'. This file contains all the actions that are and not allowed such as mass scraping. TripAdvisor opposed quite many ethical and legal implications that's why I tried to find another way for this to work. WIth the help of AI Claude's model SOnnet 4.5 i came accross 3rd party service SerpAPI. Although this resulted in poor search parameters where reviews could not be extracted
- [Why didn't it return the expected output?]: Few available credits meant I couldn't run the script as many times it needed. In general TripAdvisor proved to be a poor choice for beach reviews, as it only showed places and businesses rather than attractions and natural features.

**Learning:** Web scraping is highly dependent on website structure, which can change frequently. Anti-scraping measures and dynamic content loading can make extraction difficult.

---

### Approach 2: Google Places API (Successful Implementation)

**Objective:** Extract beach data including ratings, review counts, and keyword mentions

**Tools Used:**
- Google Places API
- Python libraries: requests, pandas, json


**Why This Worked:**
- Official API with clear documentation
- Structured JSON responses
- Reliable authentication and rate limits
- Good coverage of Italian beaches

**Data Extracted:**
1. **Ratings:** User ratings (e.g., 4.5, 5.0)
2. **Review Counts:** Number of reviews per beach (e.g., 23, 658)
3. **Keywords:** Mentions of "clean", "dirty", "plastic", "pollution", etc. also in Italian

---

## 💻 Implementation

### Notebooks

#### [`trip_reviews.ipynb`](trip_reviews.ipynb)
- **Purpose:** Initial TripAdvisor scraping attempt
- **Status:** Functional code but unsuccessful output
- **Key Learning:** Understanding web scraping limitations

#### [`google_maps_reviews_words.ipynb`](google_maps_reviews_words.ipynb)
- **Purpose:** Google Places API implementation with keyword extraction
- **Status:** ✅ Successful
- **Key Features:**
  - API authentication and request handling
  - Parameter configuration (location, radius, type)
  - JSON response parsing
  - Keyword extraction from review text
  - Data export to structured format

#### [`clean_coords.ipynb`](clean_coords.ipynb)
- **Purpose:** Coordinate data cleaning and validation
- **My Contribution:** Option 2 implementation: sets a spatial exten between Italian region, with more time I would like to add the option to sepparate north vs south for a more analysis freindly approach

---

## 📊 Data Cleaning Process

### Step 1: API Response Parsing
```python
# Example workflow (pseudocode from colab notebook)
# 1. Make API request
response = google_places_api.search(location="Italy", type="beach")

# 2. Extract relevant fields
beach_data = {
    'name': response['name'],
    'rating': response['rating'],
    'review_count': response['user_ratings_total'],
    'location': response['geometry']['location']
}
```

### Step 2: Keyword Extraction
- Searched review text for pollution-related keywords
- Keywords targeted: "clean", "dirty", "plastic", "pollution", [Italian words searched as well]
- Limitation: No sentiment analysis due to time constraints

### Step 3: Data Structuring
- Exported to tabular format (CSV/DataFrame)
- Ensured compatibility with geospatial libraries (coordinate formatting)
- Merged with beach location dataset

### Step 4: Quality Checks
- Handled missing values
- Validated coordinate formats
- Ensured locations within Italian region

---


### Data Quality
**Strengths:**
- Structured, reliable data from official API
- Good geographic coverage of tourist beaches
- Accurate rating scale
- Impemented letter by letter searching instead of whole words for example searching for plast rather than plastic or plastics

**Limitations:**
- API rate limits restricted total number of beaches
- Keyword extraction without sentiment analysis may miss context, could not be added to final results
- Bias toward popular, tourist-heavy beaches
- Language barriers (reviews in Italian required keyword translation), worked around that

### Example Output Table

| Beach Name | Rating | Reviews | Clean Mentions | Dirty Mentions | Plastic Mentions | Latitude | Longitude |
|------------|--------|---------|----------------|----------------|------------------|----------|-----------|
| Spiaggia di Mondello|   4.5   |       658      | 12 | 3 | 2 |     4     |       7        |


---

## 📝 Conclusions

### On the Results
- Successfully developed a working web scraping/API workflow that extracted meaningful data about Italian beaches
- Google Places API proved more reliable than web scraping for this use case
- Keyword extraction provided basic insights into pollution mentions, though sentiment analysis would have been ideal
- The cleaned, structured dataset was successfully integrated with geospatial data for mapping

### On Goal Accomplishment

**What worked well:**
✅ Learned to read and implement API documentation independently  
✅ Successfully extracted ratings, review counts, and keywords  
✅ Developed data cleaning workflow for coordinate validation  
✅ Created analysis-ready, structured dataset  
✅ Adapted strategy when initial approach (TripAdvisor) failed  

**What could be improved:**
- Implement full sentiment analysis instead of basic keyword matching
- Expand beyond English keywords to include Italian terms
- Develop more sophisticated text analysis (NLP techniques)
- Better error handling for API rate limits

**Did I achieve my goal?**  
**Yes, achieved.** I successfully developed a web scraping/API workflow that extracts selected indicators (ratings, reviews, keywords) and exports them into a structured, analysis-ready table. While I pivoted from web scraping to API use. The data was successfully linked to our geospatial dataset for analysis and storymap.

---

## 🎓 Key Learnings

1. **API Documentation:** Reading official documentation is a critical skill for independent data acquisition
2. **Adaptability:** When one approach fails, evaluate alternatives quickly
3. **Parameter Tuning:** Understanding API parameters (location, radius, type) enables precise data extraction
4. **Data Quality:** Always assess limitations of your data sources (bias, coverage, completeness)
5. **Context Matters:** Keyword extraction without sentiment analysis has limitations

---

## 🔗 Related Goals
- [Goal 1: Data Sources](../goal-1-data-sources/) - Identifying and evaluating data sources
- [Goal 3: Visualization](../goal-3-visualization/) - Using extracted data for storytelling

---

**Reflection:** This goal was the most technically challenging and rewarding. The failure of the TripAdvisor approach and successful pivot to Google Places API taught me resilience and the importance of having backup strategies in projects.
