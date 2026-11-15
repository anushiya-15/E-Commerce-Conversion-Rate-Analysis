# 🛒 E-Commerce Conversion Rate Analysis

## 1. Project Overview
E-Commerce Conversion Rate Analysis is a data analytics project that focuses on understanding customer shopping behaviour and analyzing the conversion journey on a generic online shopping platform.

The project examines how customers move through different shopping stages, from visiting the platform to completing a purchase.

It uses interactive Power BI dashboards to identify conversion rates, customer drop-offs, device performance, traffic channel performance, and A/B testing results.

## 2. Why This Data Was Analyzed
Not every customer who visits an online shopping platform completes a purchase.

Understanding where customers leave the shopping journey is important for improving the shopping experience and increasing business conversions.

This project was developed to analyze customer behaviour, identify stages with high drop-off rates, and understand factors that influence purchase completion.

## 3. Project Objectives
- Calculate the total number of shopping sessions and purchases.
- Analyze customer conversion rates.
- Understand the customer shopping funnel.
- Identify customer drop-off points.
- Compare mobile and desktop performance.
- Analyze conversion performance across traffic channels.
- Compare A/B testing variants.

## 4. Tools and Technologies
- **Python:** Initial dataset inspection and cleaning.
- **Power BI:** Interactive dashboard development.
- **Power Query:** Data transformation and preparation.
- **DAX:** Calculated measures and conversion rate analysis.
- **Microsoft Excel/CSV:** Dataset handling.

## 5. Dataset Description
The project uses two datasets:

### A. Shop Sessions
Contains session-level information:
- Session ID
- Session Start Time
- Traffic Channel
- Device
- A/B Testing Variant
- Basket Value

### B. Funnel Events
Contains customer shopping journey information:
- Session ID
- Step Number
- Shopping Stage
- Event Timestamp
- Cart Value

## 6. Customer Shopping Journey
The analysis follows six major shopping stages:

1. Landing
2. Product View
3. Add to Cart
4. Checkout Start
5. Payment Information
6. Purchase

## 7. Project Workflow
1. Inspected both datasets using Python.
2. Checked missing values and duplicate records.
3. Cleaned and prepared the datasets.
4. Imported the cleaned datasets into Power BI.
5. Established relationships between the tables.
6. Created DAX measures for sessions, purchases, and conversion rates.
7. Designed three interactive dashboard pages.
8. Analyzed customer behaviour and funnel performance.

## 8. Dashboard Pages

### Page 1: E-Commerce Conversion Overview
- Total Sessions
- Total Purchases
- Conversion Rate
- Product Views
- Add to Cart
- Checkout Sessions
- Shopping Sessions by Channel
- Conversion Rate by Device

### Page 2: E-Commerce Funnel Analysis
- Customer Shopping Funnel
- Sessions at Each Funnel Stage
- Stage Conversion Rates
- Customer Drop-off
- Overall Purchase Conversion

### Page 3: Customer Behaviour and Insights
- Customer Sessions by Device
- Purchases by Traffic Channel
- Average Basket Value by Device
- A/B Variant Performance
- Total Basket Value

## 9. Key Findings
The analyzed dataset contains:
- Total Sessions: 420
- Total Purchases: 22
- Overall Conversion Rate: 5.24%
- Product Views: 193
- Add to Cart: 137
- Checkout Starts: 84
- Payment Information Events: 50

The funnel analysis shows how the number of sessions decreases across successive shopping stages.

## 10. Project Outcome
Developed a three-page interactive Power BI dashboard to analyze e-commerce conversion performance, customer shopping behaviour, funnel drop-offs, and A/B testing variants.

## 11. Project Files
- Cleaned Shop Sessions Dataset
- Cleaned Funnel Events Dataset
- Python Cleaning Script
- Power BI Dashboard (.pbix)
- Dashboard Screenshots

## 12. Conclusion
This project demonstrates how data analytics and business intelligence tools can be used to understand customer shopping behaviour, identify conversion challenges, and generate insights for improving the online shopping experience.
