from torch.utils.data import Dataset
from torchvision import transforms
import pandas as pd
import numpy as np

class TripletFaceDataset(Dataset):
    
    def __init__(self, root_dir, csv_name, num_triplets, transform=None):
        self.root_dir = root_dir
        self.df = pd.read_csv(csv_name)
        self.num_triplets = num_triplets
        self.transform = transform
        self.training_triplets = self.generate_triplets(self.df, self.num_triplets)
        

    @staticmethod
    def generate_triplets(df, num_triplets):
        
        def make_dictionary_for_face_class(df):
            face_classes = dict()
            for idx, label in enumerate(df['class']):
                if label not in face_classes:
                    face_classes[label] = []
                face_classes[label].append((df.iloc[idx]['id'], df.iloc[idx]['ext']))
            return face_classes
        
        triplets = []
        classes = df['class'].unique()
        face_classes = make_dictionary_for_face_class(df)

        for _ in range(num_triplets):
            '''
              - randomly choose anchor, positive and negative images for triplet loss
              - anchor and positive images in pos_class
              - negative image in neg_class
              - at least, two images needed for anchor and positive images in pos_class
              - negative image should have different class as anchor and positive images by definition
            '''

            pos_class = np.random.choice(classes)
            neg_class = np.random.choice(classes)

            while len(face_classes[pos_class]) < 2:
                pos_class = np.random.choice(classes)

            while pos_class == neg_class:
                neg_class = np.random.choice(classes)

            pos_name = df.loc[df['class'] == pos_class, 'name'].values[0]
            neg_name = df.loc[df['class'] == neg_class, 'name'].values[0]

            if len(face_classes[pos_class]) == 2:
                ianc, ipos = np.random.choice(2, 2, replace=False)
            else:
                ianc = np.random.randint(0, len(face_classes[pos_class]))
                ipos = np.random.randint(0, len(face_classes[pos_class]))
                while ianc == ipos:
                    ipos = np.random.randint(0, len(face_classes[pos_class]))
            ineg = np.random.randint(0, len(face_classes[neg_class]))
            
            anc_id = face_classes[pos_class][ianc][0]
            anc_ext = face_classes[pos_class][ianc][1]
            pos_id = face_classes[pos_class][ipos][0]
            pos_ext = face_classes[pos_class][ipos][1]
            neg_id = face_classes[neg_class][ineg][0]
            neg_ext = face_classes[neg_class][ineg][1]

            triplets.append([anc_id, pos_id, neg_id, pos_class, neg_class, pos_name, neg_name, anc_ext, pos_ext, neg_ext])
        return triplets
    
def main():
    trip = TripletFaceDataset("./lfw", "./train_dataset.csv", 200)
    print(trip.training_triplets)
    pass

main()