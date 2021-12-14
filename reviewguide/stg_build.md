# Review points with stg

When a PR is created, a stg URL is built with the updates in the PR.

![image-20211116113538440](./media/stg.png)

To check how the update looks on docs.tizen.org, use the stg URL.

![image-20211116113814486](./media/stg_url.png)

- Because of the capacity issue, the stg URL are deleted after some days. To check the stg URL of old PR, trigger the stg build again by closing and reopening the PR.

   ![image-20211116114722738](./media/stg_rebuild.png)

- Sometimes the stg build fails. In that case, ask iljooo.kim to check the build of tizen-docs git repository