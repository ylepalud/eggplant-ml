### Configuration

This project need a .env file with this shape in order to work

# Database configuration
DB_URL=
DB_PORT=

# RabbitMq configuration
RABBIT_MQ_HOST=
RABBIT_MQ_PORT=
RABBIT_MQ_SERVER=

# Build and run with docker
docker build -t eggplant .
docker run -it -env-file .env --name moussaka eggplant

