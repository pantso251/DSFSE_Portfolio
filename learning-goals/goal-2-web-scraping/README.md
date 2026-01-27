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
- Python libraries: BeautifulSoup, requests
- [ADD: Other libraries you used]

**Outcome:** Code executed successfully but did not return the desired output

**Challenges:**
- [ADD: What specific issues did you encounter? Dynamic content? Anti-scraping measures?]
- [ADD: Why didn't it return the expected output?]

**Learning:** Web scraping is highly dependent on website structure, which can change frequently. Anti-scraping measures and dynamic content loading can make extraction difficult.

---

### Approach 2: Google Places API (Successful Implementation)

**Objective:** Extract beach data including ratings, review counts, and keyword mentions

**Tools Used:**
- Google Places API
- Python libraries: requests, pandas, json
- [ADD: Other libraries]

**Why This Worked:**
- Official API with clear documentation
- Structured JSON responses
- Reliable authentication and rate limits
- Good coverage of Italian beaches

**Data Extracted:**
1. **Ratings:** User ratings (e.g., 4.5, 5.0)
2. **Review Counts:** Number of reviews per beach (e.g., 23, 658)
3. **Keywords:** Mentions of "clean", "dirty", "plastic", "pollution", etc.

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
- **My Contribution:** Option 2 implementation
- **Key Features:**
  - [ADD: What did your Option 2 do specifically?]
  - Geographic coordinate validation
  - Data quality checks
  - Preparation for geospatial analysis

---

## 📊 Data Cleaning Process

### Step 1: API Response Parsing
```python
# Example workflow (pseudocode from your notebook)
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
- Keywords targeted: "clean", "dirty", "plastic", "pollution", [ADD: others]
- Limitation: No sentiment analysis due to time constraints
- Recognized that context matters (e.g., "no plastic" vs. "plastic everywhere")

### Step 3: Data Structuring
- Exported to tabular format (CSV/DataFrame)
- Ensured compatibility with geospatial libraries (coordinate formatting)
- Merged with beach location dataset

### Step 4: Quality Checks
- Handled missing values
- Validated coordinate formats
- [ADD: Other quality checks you performed]

---

## 🎯 Results

### Successful Data Extraction
- **Beaches covered:** [ADD: How many beaches?]
- **Review data points:** [ADD: Total reviews extracted]
- **Keyword mentions:** [ADD: How many keyword hits?]
- **Geographic coverage:** [ADD: Regions in Italy covered]

### Data Quality
**Strengths:**
- Structured, reliable data from official API
- Good geographic coverage of tourist beaches
- Consistent rating scale

**Limitations:**
- API rate limits restricted total number of beaches
- Keyword extraction without sentiment analysis may miss context
- Bias toward popular, tourist-heavy beaches
- Language barriers (reviews in Italian required keyword translation)

### Example Output Table

| Beach Name | Rating | Reviews | Clean Mentions | Dirty Mentions | Plastic Mentions | Latitude | Longitude |
|------------|--------|---------|----------------|----------------|------------------|----------|-----------|
| [Example] | 4.5 | 658 | 12 | 3 | 2 | 43.xxxx | 10.xxxx |

[ADD: A real example or screenshot if available]

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
**Yes, achieved.** I successfully developed a web scraping/API workflow that extracts selected indicators (ratings, reviews, keywords) and exports them into a structured, analysis-ready table. While I pivoted from web scraping to API use, this demonstrates adaptability and problem-solving. The data was successfully linked to our geospatial dataset for analysis.

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

**Reflection:** This goal was the most technically challenging and rewarding. The failure of the TripAdvisor approach and successful pivot to Google Places API taught me resilience and the importance of having backup strategies in data science projects.