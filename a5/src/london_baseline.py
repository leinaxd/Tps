# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

if __name__ == "__main__":
    predictions = []
    for line in open(args.eval_corpus_path):
        predictions.append("London")
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)

    if total > 0:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
    else:
        print('no targets provided')