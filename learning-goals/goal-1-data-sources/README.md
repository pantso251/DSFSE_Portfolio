# Goal 1: Finding Suitable Data Sources

**Category:** Data acquisition, wrangling, storing

---

## 🎯 Original Goal Statement

**Goal:** Within this course, I want to independently identify and locate suitable environment-related data sources for our group project. Following that, proper storing and processing will take place through a git version control system.

**How:** Selected sources will be stored in the team's database and all processing followed will be documented in `.ipynb` scripts with strong and supportive comments and notations.

---

## 📋 Background

For the beach pollution analysis project in Italy, we needed multiple data sources that could provide:
- Geospatial information about beach locations
- User-generated content about beach quality
- Environmental indicators related to pollution, WWF dataset only provides 6 major material categories and the number found in all beaches
- Temporal data to track changes over time, WWF dataset was still incomplete, we only managed to capture few months of where data collection is visible

Unlike previous courses where clean, pre-packaged datasets were provided, this project required independent research, evaluation, and acquisition of raw data sources.

---

## 🔍 Methodology

### Data Source Selection Criteria
1. **Relevance:** Must relate to beach quality, pollution, or environmental conditions in Italy
2. **Accessibility:** Must be obtainable through APIs, web scraping, or public datasets
3. **Quality:** Must have sufficient coverage and reliability for analysis
4. **Compatibility:** Must be integrable with geospatial analysis tools (Python, GeoPandas, GeoDA, ArcGIS etc.)

### Data Sources Identified

#### 1. Google Places API
- **Purpose:** Extract beach ratings, review counts, and user-generated keywords
- **Why Selected:** Real-time, crowdsourced data; good geographic coverage; accessible via API, hidden as a secret
- **Format:** JSON responses from API calls
- **Limitations:** Rate limits; requires API key; may have bias toward tourist areas


## 💾 Data Storage and Version Control

### Git Implementation Challenges
- **Challenge:** Not all team members were familiar with Git version control
- **Impact:** Limited systematic version control implementation
- **Workaround:** Used Google Colab for collaborative notebook editing; manual file sharing
-

### Data Organization
- Notebooks stored in shared repository structure
- Data files managed through [ADD: How you managed data files - Google Drive, local storage, etc.]
- Processing steps documented with comments in `.ipynb` notebooks

---

## 📊 Implementation

### Notebooks Related to This Goal
- [`google_maps_reviews_words.ipynb`](../goal-2-web-scraping/google_maps_reviews_words.ipynb) - Google Places API data extraction
- [`clean_coords.ipynb`](../goal-2-web-scraping/clean_coords.ipynb) - Coordinate data cleaning and validation
- [ADD: Any other notebooks related to data acquisition]

### Key Code Examples

**Example: Data source evaluation decision-making**
```python
# Initially attempted TripAdvisor scraping
# Pivoted to Google Places API due to:
# 1. Better documentation
# 2. More reliable data structure
# 3. Easier authentication process
```

[ADD: Code snippets showing how you evaluated or accessed data sources]

---

## 🎯 Results

### Data Sources Successfully Acquired
✅ Google Places API data for Italian beaches  
✅ Beach coordinate datasets  
✅ [ADD: Other successful data acquisitions]

### Data Quality Assessment
- **Coverage:** [How many beaches? Geographic spread?]
- **Completeness:** [Missing data? Gaps?]
- **Reliability:** [How did you assess data quality?]

---

## 📝 Conclusions

### On the Results
- Successfully identified and acquired multiple relevant data sources for beach pollution analysis
- Google Places API proved to be the most reliable source for user-generated content
- [ADD: Other key findings about your data sources]

### On Goal Accomplishment
**What worked well:**
- Independent research and evaluation of data sources
- Successfully navigated API documentation to extract meaningful data
- Adapted when initial approaches (TripAdvisor) didn't work as expected

**What could be improved:**
- More systematic Git version control implementation (team skill gaps limited this)
- Could have explored additional environmental datasets (e.g., satellite data, official pollution reports)
- Better documentation of data source evaluation process from the beginning

**Did I achieve my goal?**  
**Partially achieved.** I successfully identified and acquired suitable data sources independently, and documented processing in notebooks with clear comments. However, the Git version control implementation was limited due to team constraints. Despite this, I learned valuable lessons about data source evaluation, API integration, and the importance of adaptability in data acquisition.

---

## 🔗 Related Goals
- [Goal 2: Web Scraping and Cleaning](../goal-2-web-scraping/) - Implementation of data extraction workflows
- [Goal 3: Visualization](../goal-3-visualization/) - Using acquired data for storytelling

---

**Reflection:** This goal taught me that finding suitable data is often more challenging than analyzing it. The process of evaluating sources, understanding their limitations, and adapting when initial approaches fail is a critical skill in data science.
