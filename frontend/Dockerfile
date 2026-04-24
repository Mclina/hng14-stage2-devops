FROM node:18-slim

WORKDIR /app

COPY package*.json ./
RUN npm install --production

# Security: Use the built-in 'node' user
RUN chown -R node:node /app
USER node

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
