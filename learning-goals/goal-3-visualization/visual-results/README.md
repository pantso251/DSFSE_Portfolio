# Visual Results - Beach Pollution Analysis

This folder contains the key visualizations from the project, explaining beach pollution patterns in Italy.

---

## 📊 Visualization Overview

All figures are designed to be accessible to non-technical audiences including policymakers and students.

**Note:** Most of the maps produced are in screenshots due to ArcGIS web feature layers not being able to be shared to other users. Seperate folder holds a gdb file for ArcGis Pro, where layers and outputs contain proper geometry and metadata of files.

---

## Metadata of Visualizations
**GeoDA Table to Points - Italy (geoda_table-to-points-it)**

What this shows: 
This map displays the spatial distribution of individual beach location accross the Italian region where data was collected. Points were gathered and inserted in the GeoDA software for a quick visualization. Each point represents a beach location derived from the WWF dataset after preprocessing and parsing of coordinates took place. Showing the geographic coverage of the dataset.

    Key findings: 
    -Beach data coverage is concentrated along popular tourist coastlines, particularly in regions like Tuscany, Liguria, and Puglia, where data was found in abundance

    -Notable gaps are identified at less touristed coastal areas, revealing a spatial bias towards high-traffic beaches

    -The point distribution explains where tourists would leave beach reviews instead of pollution data. 

---
**Italian Beaches Heatmap v4 (it-beaches-heatmap-v4)**
What this shows: 

A density map visualizing the concenrtation of beaches with highest pollution count accross Italy. Warm colours(red/orange) indicate higher concentrations of beaches where aggregated materials in total were used as a weight field in layer creation. 

    Key findings: 
    -Distinct pollution hotspots emerge in high-traffic tourist regions along the Adriatic coast and around major urban centers

    -Southern Italian beaches show varied patterns, with some areas having concentrated values for smaller beaches

    -Coastal areas near cities display higher density count of pollution this was also shown during extract keyewords from google reviews.

---

**Italian Density Story Map (it-density-story-map)**

What the visualization shows:
An interactive story map that combines spatial density visualization with interactive elements, immersing viewers through the patterns of beach pollution concentration across different Italian regions. Note it is the same output of it-beaches-heatmap-v4 but for story map purposses.

---

**Italian Onion Hotspot 10km (it-onion-hotspot-10km)**

What this shows:
A hotspot analysis ([ArcGis geostatistical analysis tool](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/spatial-statistics/hot-spot-analysis.htm)) using a 10-kilometer search radius that identifies statistically significant clusters of beaches with elevated pollution concerns. The "onion" layering shows graduated intensity levels within hotspot zones.

    Key findings:
-Statistically significant pollution hotspots are confirmed around major coastal cities including Rimini, Venice, and Naples areas

    -The 10km radius reveals regional-scale pollution patterns rather than individual beach problems

    -Hotspots often extend along continuous coastline stretches, suggesting systematic regional environmental challenges rather than individual action models. This implies that a natural reserve such as a park or river exists nearby calling for immediate action.
Explanation:
For policymakers, this identifies where coordinated regional responses are needed rather than fixing individual beaches. If you see a hotspot covering multiple municipalities, those local governments should work together on solutions like improved waste management infrastructure, better beach monitoring, or tourism management strategies.

---

**Italian Onion Hotspot 2km (it-onion-hotspot-2km)**

What this visualization shows:
This is the main visualization where it shows to the Italian policy makers where to take action. This fine-scale hotspot analysis uses a 2-km search radius that pinpoints possible localized pollution areas. The higher-resolution spatial assessment refined at 2km reveals individual beach clusters and specific segemnts with elevated concerns. 

    Key findings: 
    -Precise problem locations emerge at the individual beach or small coastal segment level

    -Many hotspots correspond to beaches near river mouths, ports, or urban drainage outlets

    -Some isolated tourist beaches show unexpected hotspots, suggesting localized infrastructure problems or inadequate waste management for visitor volumes

**Explanation for policymakers and non-technical audiences**:

This is the detailed, close-up version of the pollution hotspot map, focusing on specific problem beaches within 2 kilometers of each other. While the 10km map showed regional problems, this map identifies exactly which beaches need immediate attention. The onion rings show precisely where more systematic cleaning efforts would help prevent future pollution. This can be achieved by adding more trash cans or by sending multiple cleaning crews throughout the summer high-season. If a town is shown in the hotspot zone it means where visitor are possibly complaining more about the beach than statistically expected. That is where an oppurtunity arises, by addressing these locations it is highly expected to improve both environmental quality and tourism reputation.

---

## 📌 Notes

- All maps created using ArcGIS Pro/ArcGIS Online and Plotly
- Data represents crowdsourced beach reviews and ratings
- Density calculations show concentration patterns, not absolute pollution measurements

---

