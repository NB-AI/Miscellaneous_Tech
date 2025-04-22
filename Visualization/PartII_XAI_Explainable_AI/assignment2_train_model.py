import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from sklearn.metrics import confusion_matrix
from tqdm import tqdm


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.pre_trained = torchvision.models.resnet18(pretrained=True)
        self.pre_trained.fc = nn.Linear(512, 6)
    
    def forward(self, x):
        x = self.pre_trained(x)
        return x

train_transform = transforms.Compose(
    [transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])])
val_test_transform = transforms.Compose(
    [transforms.Resize((224,224)),
     transforms.ToTensor(),
     transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])])

train_dataset = torchvision.datasets.ImageFolder(root='./dataset/train/', transform=train_transform)
test_dataset = torchvision.datasets.ImageFolder(root='./dataset/test/', transform=val_test_transform)

# split train_dataset into train and val
train_size = int(0.8 * len(train_dataset))
val_size = len(train_dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(train_dataset, [train_size, val_size])

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=1)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=32, shuffle=True, num_workers=1)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=True, num_workers=1)


def train(model, train_loader, val_loader, test_loader, criterion, optimizer, num_epochs=10):
    train_loss = []
    val_loss = []
    train_acc = []
    val_acc = []
    best_acc = 0.0
    true_labels = []
    pred_labels = []
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        running_corrects = 0

        # Initialize the progress bar for the training phase
        progress_bar = tqdm(train_loader, desc='Training')
        for inputs, labels in progress_bar:
            inputs = inputs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            _, preds = torch.max(outputs, 1)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            
            # Update the progress bar description
            progress_bar.set_description(
                f'Epoch {epoch+1}/{num_epochs} - Train Loss: {loss.item():.4f}, Acc: {torch.sum(preds == labels.data).double() / inputs.size(0):.4f}')

        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_acc = running_corrects.double() / len(train_loader.dataset)
        train_loss.append(epoch_loss)
        train_acc.append(epoch_acc)
        print(f'Epoch {epoch+1} - Train Loss: {epoch_loss:.4f}, Train Acc: {epoch_acc:.4f}')

        model.eval()
        running_loss = 0.0
        running_corrects = 0


        # Initialize the progress bar for the validation phase
        progress_bar_val = tqdm(val_loader, desc='Validation')
        for inputs, labels in progress_bar_val:
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            _, preds = torch.max(outputs, 1)
            true_labels.append(labels)
            pred_labels.append(preds)
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)

            # Update the progress bar description
            progress_bar_val.set_description(
                f'Epoch {epoch+1}/{num_epochs} - Val Loss: {loss.item():.4f}, Acc: {torch.sum(preds == labels.data).double() / inputs.size(0):.4f}')

        epoch_loss = running_loss / len(val_loader.dataset)
        epoch_acc = running_corrects.double() / len(val_loader.dataset)
        val_loss.append(epoch_loss)
        val_acc.append(epoch_acc)
        print(f'Epoch {epoch+1} - Val Loss: {epoch_loss:.4f}, Val Acc: {epoch_acc:.4f}')
        if epoch_acc > best_acc:
            best_acc = epoch_acc
            torch.save(model.state_dict(), 'best_resnet18.pth')
            print("Model saved")
    print("Training completed")

    # load best model weights
    model.load_state_dict(torch.load('best_resnet18.pth'))
    model.eval()
    running_loss = 0.0
    running_corrects = 0
    true_labels = []
    pred_labels = []
    # Initialize the progress bar for the test phase
    progress_bar_test = tqdm(test_loader, desc='Test')

    for inputs, labels in progress_bar_test:
        inputs = inputs.to(device)
        labels = labels.to(device)
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        _, preds = torch.max(outputs, 1)
        true_labels.append(labels)
        pred_labels.append(preds)
        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)

        # Update the progress bar description
        progress_bar_test.set_description(
            f'Test Loss: {loss.item():.4f}, Acc: {torch.sum(preds == labels.data).double() / inputs.size(0):.4f}')
    
    epoch_loss = running_loss / len(test_loader.dataset)
    epoch_acc = running_corrects.double() / len(test_loader.dataset)
    print(f'Test Loss: {epoch_loss:.4f}, Test Acc: {epoch_acc:.4f}')
    # plot confusion matrix
    true_labels = torch.cat(true_labels)
    pred_labels = torch.cat(pred_labels)
    cm = confusion_matrix(true_labels.cpu(), pred_labels.cpu())
    columns = ["forest", "buildings", "glacier", "mountain", "sea", "street"]
    df_cm = pd.DataFrame(cm, index = columns,
                  columns = columns)
    plt.figure(figsize = (10,7))
    sns.heatmap(df_cm,annot=True,cmap='Blues', fmt='g')
    plt.savefig("confusion_matrix.png")


    return train_loss, val_loss, train_acc, val_acc

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net()
model = model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
train_loss, val_loss, train_acc, val_acc = train(model, train_loader, val_loader, test_loader, criterion, optimizer, num_epochs=10)

# plot train and val loss
plt.figure()
plt.plot(train_loss, label="train loss")
plt.plot(val_loss, label="val loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.savefig("loss.png")

