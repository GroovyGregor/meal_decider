#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:13:03 2017

@author: gregor-linux
"""
import pandas as pd
import numpy as np


# =============================================================================
# Input
# =============================================================================
meal_type_file = 'meal_type.csv'
meal_rating_file = 'taste_rating.csv'
meal_health_file = 'health_rating.csv'

# Open files
with open(meal_type_file) as type_f:
    meal_type = pd.read_csv(type_f, dtype='str')
with open(meal_rating_file) as rating_f:
    meal_rating = pd.read_csv(rating_f)
with open(meal_health_file) as health_f:
    meal_health = pd.read_csv(health_f)


# =============================================================================
# Calculate rating
# =============================================================================
# Get meal names
meals = list(meal_rating)

# Get mean rating
mean_rating = meal_rating.mean()

# Calculate effective rating
for meal in meals:

    # Consider health of meal
    mean_rating[meal] *= meal_health[meal].mean()

    # Consider type of meals
    if meal_type[meal].values[0] == 'vegetarian':
        mean_rating[meal] *= 0.5
    elif meal_type[meal].values[0] == 'meat':
        mean_rating[meal] *= 0.1
    else:
        assert meal_type[meal].values[0] == 'Vegan', 'Type of meal not vegan, \
            vegatarian or meat - check type of meals'

# Calculate total rating points
rating_sum = mean_rating.sum()
rating_sum = rating_sum*10/9  # 10% for trying out new meals

mean_rating = mean_rating.fillna(0)

# Create list of probabilities
prob = list(mean_rating/rating_sum)

# Append entriees for new meals with probability of 10%
prob.append(0.1)
meals.append('new')

# Choose a weighted random meal
next_meal = np.random.choice(meals, 1, p=prob)

print(next_meal[0])
