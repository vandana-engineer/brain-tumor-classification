from model import build_model

def train():
    model = build_model()

    print("Training started...")

    # Placeholder for dataset loading
    # model.fit(X_train, y_train)

    model.save("../data/models/brain_tumor_model.h5")

    print("Model saved successfully!")

if __name__ == "__main__":
    train()
