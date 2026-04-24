# Build Stage
FROM node:18-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Production Stage
FROM node:18-slim
WORKDIR /app
RUN useradd -m frontenduser
USER frontenduser
COPY --from=build /app .
EXPOSE 3000
CMD ["npm", "start"]
