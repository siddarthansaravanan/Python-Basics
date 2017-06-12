drc = 'train/'
images = [drc + f for f in os.listdir(drc)]
train_labels = []
for f in images:
    train_labels.append(f.split('/')[-1])