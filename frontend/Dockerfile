FROM node:10.15.0

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install

EXPOSE 8081
CMD [ "http-server", "-p 8081", "dist" ]
CMD ["npm", "run", "serve", "--", "--port", "8081"]
