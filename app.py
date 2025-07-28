name: Azure Docker CI/CD

on:
  push:
    branches:
      - main

jobs:
  checkout:
    name: 📥 Checkout Code
    runs-on: ubuntu-latest
    outputs:
      tag: ${{ steps.set_tag.outputs.image_tag }}
    steps:
      - uses: actions/checkout@v3

      - name: 🏷️ Get Commit Message as Image Tag
        id: set_tag
        run: |
          RAW_TAG=$(git log -1 --pretty=%s)
          CLEAN_TAG=$(echo "$RAW_TAG" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9-_' | cut -c1-40)
          echo "image_tag=$CLEAN_TAG"
          echo "image_tag=$CLEAN_TAG" >> $GITHUB_OUTPUT

  login:
    name: 🔐 ACR Login
    runs-on: ubuntu-latest
    needs: checkout
    steps:
      - name: Login to Azure Container Registry
        uses: azure/docker-login@v1
        with:
          login-server: ${{ secrets.ACR_LOGIN_SERVER }}
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}

  build:
    name: 🛠️ Docker Build
    runs-on: ubuntu-latest
    needs: [checkout, login]
    env:
      IMAGE_NAME: rajveerapp
      ACR_SERVER: ${{ secrets.ACR_LOGIN_SERVER }}
      IMAGE_TAG: ${{ needs.checkout.outputs.tag }}
    steps:
      - uses: actions/checkout@v3

      - name: 🔧 Build Docker Image
        run: |
          echo "📌 IMAGE TAG: $IMAGE_TAG"
          echo "📌 FULL IMAGE: $ACR_SERVER/$IMAGE_NAME:$IMAGE_TAG"
          docker build -t $ACR_SERVER/$IMAGE_NAME:$IMAGE_TAG .

  push:
    name: 📤 Docker Push
    runs-on: ubuntu-latest
    needs: build
    env:
      IMAGE_NAME: rajveerapp
      ACR_SERVER: ${{ secrets.ACR_LOGIN_SERVER }}
      IMAGE_TAG: ${{ needs.checkout.outputs.tag }}
    steps:
      - name: 📦 Push Docker Image to ACR
        run: |
          echo "📤 Pushing image: $ACR_SERVER/$IMAGE_NAME:$IMAGE_TAG"
          docker push $ACR_SERVER/$IMAGE_NAME:$IMAGE_TAG
