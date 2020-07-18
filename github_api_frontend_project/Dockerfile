FROM nginx:1.15.2-alpine

ARG REACT_APP_GRAPHQL_ENDPOINT_ARG
ENV REACT_APP_GRAPHQL_ENDPOINT=$REACT_APP_GRAPHQL_ENDPOINT_ARG


COPY ./build /var/www
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT ["nginx","-g","daemon off;"]