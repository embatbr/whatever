The **Nubank Puzzle** is a short modeling assignment that is typical of some of the work we do at Nubank. It should only take you **1-2 hours**, but feel free to spend more time on it if you wish.

We host a ZIP archive [here](https://s3-sa-east-1.amazonaws.com/nu-static/workable-data-science/data-science-puzzle.zip) that contains 3 CSV files: **train.csv**, **test.csv**, and **sample_submission.csv**. **train.csv** contains a column called `id` which uniquely identifies each row, several columns identified by hexadecimal strings, and a column `target` which we would like for you to predict. Columns that contain SHA-256 hashes for their values represent categorical variables, while the rest of the variables are numeric. **test.csv** has the same column names and data types as **train.csv**, but it is missing the `target` column. There are no missing values or data corruption problems in either of these files. Do not worry about the meanings of the variables or the metadata -- this is an artificial dataset.

You can use any programming language and modeling approach you choose. You will be evaluated primarily on the *R²* of your predictions against the true values in the test set, but the accuracy of your estimate of your *R²* will also be considered. You can find an explanation of the *R²* metric [here](https://en.wikipedia.org/wiki/Coefficient_of_determination).

Please submit your predictions as a CSV file. You should include a header with columns as below and put the `id` and your predicted target for each corresponding row from the **test.csv** file. **sample_submission.csv** gives an example of what your submission file should look like.

```
id,prediction
```

Please submit your prediction CSV file and source code we can use to reproduce your submission in a ZIP file. Please put your prediction CSV file in the root of the archive. The only file in the archive with a **.csv** file extension should be your predictions.

To submit your solution, please email **Kevin Bird** at kevin.bird@nubank.com.br with a short explanation of what you did and what you expect the *R²* to be for your predictions, and attach the ZIP file with your predictions and source code. If you have any feedback or questions, feel free to email **Kevin** as well.

Good luck and we are excited to get to know you better ;-)
