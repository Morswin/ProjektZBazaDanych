FROM node:lts as build  
# https://docs.astro.build/en/recipes/docker/
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM node:lts AS runtime

WORKDIR /app

COPY --from=build /app/dist ./dist

COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package*.json ./

ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
