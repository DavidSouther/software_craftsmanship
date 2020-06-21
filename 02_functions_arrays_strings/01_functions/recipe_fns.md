# One way to break out functions:

1.  Functions for each recipe. Recipes are "hard coded", so there's not much
    it can do. Each list of ingredients will need to be bundled together into a
    function. Each of these functions will take one input, `desired_servings`,
    and prints out each ingredient scaled to the appropriate amount.

1.  One function to ask the user which recipe they would like and the number of
    desired servings, which then based on the user's selection calls the correct
    recipe function made above.

1.  One function for each category of measurements, like volume, or count, or
    weight. This function will take the scale, the measurement, and the
    ingredient name as input. It will scale the measurement, apply appropriate
    conversions between units like tablespoons to teaspoons, and print out the
    scaled value in appropriate units.