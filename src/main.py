import boto3
import time

cloudfront = boto3.client('cloudfront')

def invalidate_distribution_by_origins(domain_name):
    distributions = cloudfront.list_distributions()['DistributionList']['Items']
    for distribution in distributions:
        origins = distribution.get('Origins') and distribution.get('Origins').get('Items')
        for origin in origins:
            if domain_name in origin['DomainName']:
                distribution_id = distribution['Id']
                cloudfront.create_invalidation(
                    DistributionId=distribution_id,
                    InvalidationBatch={
                        'Paths': {
                            'Quantity': 1,
                            'Items': ['/*']
                        },
                        'CallerReference': str(time.time())
                    }
                )
                print(f"CloudFront distribution with Id: {distribution_id} has been invalidated.")
                return
    print(f"No CloudFront distribution found for domain: {domain_name}")

def invalidate_distribution_by_alias(alias):
    distributions = cloudfront.list_distributions()['DistributionList']['Items']
    for distribution in distributions:
        aliases = distribution.get('Aliases') and distribution.get('Aliases').get('Items')
        if aliases and alias in aliases:
            distribution_id = distribution['Id']
            cloudfront.create_invalidation(
                DistributionId=distribution_id,
                InvalidationBatch={
                    'Paths': {
                        'Quantity': 1,
                        'Items': ['/*']
                    },
                    'CallerReference': str(time.time())
                }
            )
            print(f"CloudFront distribution with Id: {distribution_id} has been invalidated.")
            return
    print(f"No CloudFront distribution found for alias: {alias}")


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import os
    domain_name = os.environ.get('DOMAIN_NAME')
    invalidate_distribution_by_origins(domain_name)
    invalidate_distribution_by_alias(domain_name)
