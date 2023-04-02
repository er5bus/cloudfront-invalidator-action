# Cloudfront Invalidator Action
This GitHub Action invalidates a CloudFront distribution by its origin and alias. It takes the DOMAIN_NAME environment variable as an input and uses the AWS CLI to invalidate the CloudFront distribution.

Usage
To use this action, add the following step to your workflow:

``` yaml
steps:
  - name: Invalidate CloudFront distribution
    uses: er5bus/cloudfront-invalidator-action@v1.0.0
    env:
      DOMAIN_NAME: mydomain.com
```
Make sure to replace mydomain.com with your own domain name.

Inputs
`DOMAIN_NAME` (required)

The domain name of the CloudFront distribution to invalidate.

Output
The action will output the ID of the Cloudfront distribution that was invalidated.
``` log
CloudFront distribution with Id: E1234567890ABC has been invalidated.
```

License
This action is licensed under the MIT License.
