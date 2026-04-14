## Data Cleaning & Preprocessing

To ensure accurate and meaningful analysis, the dataset was carefully cleaned and refined through the following steps:

---

### 1. Scope Definition

The dataset includes restaurants from multiple countries with varying currencies and market conditions.  
An initial analysis revealed that the dataset is highly skewed, with approximately 88% of the observations belonging to a single country (Country Code = 1).

To ensure:
- consistency in cost-based analysis (due to currency differences)
- sufficient data volume for reliable insights  

the analysis was restricted to this dominant country segment.

---

### 2. Handling Missing Values

A small number of records had missing values in the **'Cuisines'** column.  
Since these constituted a negligible portion of the dataset, such rows were removed to maintain clarity and avoid introducing non-informative categories.

---

### 3. Data Type Conversion

Relevant columns such as **rating**, **votes**, and **cost** were converted to numeric formats to enable proper statistical analysis.

---

### 4. Removing Invalid Entries

Restaurants with **rating = 0** were removed, as they represent unrated entities and do not reflect actual customer feedback.

---

### 5. Handling Outliers

The cost distribution contained extreme values (e.g., up to 800,000), which are unrealistic and could distort analysis.

To address this, outliers were removed using a **99th percentile threshold**, ensuring that extreme values do not bias results while preserving the majority of the dataset.

---

### 6. Feature Selection

Irrelevant, redundant, and non-informative columns were removed to focus on meaningful variables:

- **Identifiers**:
  - Restaurant ID (no analytical value)

- **Highly granular fields**:
  - Address (too detailed for analysis)

- **Redundant features**:
  - Locality Verbose (duplicate location information)

- **Geographic coordinates**:
  - Latitude, Longitude (not used in this analysis)

- **Currency information**:
  - Currency (analysis restricted to a single country)

- **Derived / non-informative columns**:
  - Rating color, Rating text

- **Platform-specific/UI features**:
  - Switch to order menu

- **Time-dependent features**:
  - Is delivering now (represents temporary state)

---

### 7. Final Dataset

After preprocessing, the dataset was reduced to:

- **6,473 records**
- **11 relevant features**

This refined dataset ensures a focused, consistent, and reliable foundation for exploratory data analysis.


### Cuisine Analysis – Key Insights

The cuisine distribution shows a strong concentration around a few dominant categories.

- North Indian cuisine is the most prevalent, significantly outnumbering all other cuisines.
- Chinese and Fast Food cuisines also have a strong presence, together forming the top 3 categories.

The top 3 cuisines alone account for nearly **46% of the dataset**, indicating that a large portion of restaurants focus on a limited set of popular food categories.

Additionally, the top 10 cuisines contribute approximately **75% of all restaurants**, demonstrating a clear **long-tail distribution**, where a few cuisines dominate while many others have minimal representation.

This suggests that customer demand is highly concentrated, with strong preference toward familiar and widely accepted cuisines such as North Indian and Indo-Chinese.

Overall, the market is not evenly distributed, but rather driven by a small number of high-demand cuisine types.

