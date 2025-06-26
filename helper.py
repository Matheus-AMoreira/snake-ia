import matplotlib.pyplot as plt
from IPython import display

plt.ion() # Keep this for interactive updates

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    # display.display(plt.gcf()) # Not strictly needed with %matplotlib notebook/widget as the figure is already being displayed
    plt.clf()
    plt.title('Training')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.gcf().canvas.draw() # Explicitly draw the canvas to update the plot
    # plt.gcf().canvas.flush_events() # Sometimes useful for immediate updates
    # plt.show(block=True) # Still not strictly needed, as the notebook handles display
    # plt.pause(.1) # Still not strictly needed, but can be used for very short pauses if necessary