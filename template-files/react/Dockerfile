FROM node:19-alpine

ENV PORT=80
WORKDIR /app

COPY package.json ./
COPY . ./ /app/

RUN npm install
RUN npm run build
RUN npm install -g serve

CMD ["serve", "-s", "build"]
