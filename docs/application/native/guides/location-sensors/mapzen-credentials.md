# Getting a Mapzen API Key

Mapzen products help you put a map anywhere, search and route the planet, and try a world of open data. They are built from open-source tools that are packaged into a Web service and hosted on the Mapzen servers. If you want to use Mapzen services, you must create a Mapzen developer account and a valid API key, and keep your requests to the service within certain rate limits.

> **Note**  
> Mapzen products are available for any use, including commercial purposes. You must follow the [attribution requirements](https://mapzen.com/rights/) for the data source, and also provide acknowledgment to Mapzen if you are using these Web services.

Mapzen developer account authentication is made through [GitHub](https://github.com), which is a Web site that enables people to collaborate on a project. You need a GitHub account to create a Mapzen developer account, as there is currently no other form of authentication.

To create the Mapzen API key:

1. If you do not have a GitHub account, [create it](https://github.com/join).You can create any kind of account, including personal.

2. Go to [https://mapzen.com/developers](https://mapzen.com/developers ).This is where you can create, delete, and manage your API keys.

3. Sign in with your GitHub account.

   If you are signing in for the first time, you must agree to the terms.

4. Create a new Mapzen key in the dashboard.

   The API key is a code that uniquely identifies your developer account without providing a password.

5. Optionally, give the key a name so you can remember the purpose of the project.

To use the Mapzen API key in your application, set it with the `maps_service_set_provider_key()` function:

```
maps_service_h maps = NULL;
int error = maps_service_create("MAPZEN", &maps);
error = maps_service_set_provider_key(maps, "mapzen-xxxxxx")
```

## API Rate Limits

Mapzen offers a free tier for each service, subject to rate limits. Mapzen-hosted services are shared resources, so there are limitations to prevent individual users from degrading system performance for everyone. The services have maximum numbers of queries you can make within a certain period of time, and some have additional limitations to minimize computationally intensive uses. For the current free rate limits, see [Mapzen pricing](https://mapzen.com/pricing/).

All the projects used to build the Mapzen-hosted services are open source. If you want to try Mapzen products, start with the hosted services to see if they fit your work flow needs. If you later decide that you need additional customizations or higher capacity, consider installing the open-source code used to build Mapzen services on your own servers.

If you find a problem, need higher limits, or have enhancement suggestions for Mapzen products, contact [hello@mapzen.com](mailto:hello@mapzen.com).

## API Usage Check

To check your usage for a specific API key:

1. [Sign in](https://mapzen.com/developers) to your developer account.
2. Click the **statistics** button for the API key whose usage you want to review.
3. View a graph of your recent usage for a certain period of time, such as the past day or month.

If you exceed the rate limits, the server's response to your query contains a specific [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) in the header. The typical errors for exceeded limits are "403 Forbidden" and "429 Too Many Requests".

Not all queries count towards your rate limit. Mapzen uses server caching to deliver commonly requested content as quickly as possible. Queries served from the cache are not included in the rate limit count. For example, queries can be served from the cache when the user browses a map with vector tiles in a popular extent or repeatedly performs an identical geocoding search.

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
