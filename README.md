# dockerdemo

Uses the common.yml configuration for the web and regris services.
Run `docker-compose up`.
Compose creates, links, and starts a web and redis container linked together.
It mounts your application code inside the web container.

Verify that the code is mounted by changing the message in
`app.py`&mdash;say, from `Hello world!` to `Hello from Compose!`.

Don't forget to refresh your browser to see the change!

Run `docker-compose -f production.yml up`.

    Compose creates *just* a web container and configures the Redis connection via
    the `REDIS_HOST` environment variable. This variable points to the production
    Redis instance.

    > **Note**: If you try to load up the webapp in your browser you'll get an
    > error&mdash;`redis-production.example.com` isn't actually a Redis server.

You've now done a basic `extends` configuration. As your application develops,
you can make any necessary changes to the web service in `common.yml`. Compose
picks up both the development and production environments when you next run
`docker-compose`. You don't have to do any copy-and-paste, and you don't have to
manually keep both environments in sync.
