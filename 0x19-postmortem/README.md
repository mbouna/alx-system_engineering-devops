# Server Outage Incident report
> By Mohammed BOUNA

![](https://t3.ftcdn.net/jpg/04/92/09/72/240_F_492097246_yagE8x9Uk8M9IekPy7GBuE0x1Uoa7esD.jpg)

31st January 2023, we experienced server outage on all our server infrastructure which resulted in our clients inability to use our services and we sincerely apologize for the financial loss our clients have incurred during this period.

## Issue Summary
![](https://www.cienotes.com/wp-content/uploads/2019/07/summaryblackboard.jpg)

On 31st January 2023 (10am GMT + 1), we experienced a server outage (downtime) on all of our server infrastructure which lasted for 37 minutes. As a result of this, our clients experienced a http `500 error` which had a __100% impact__ on their business as they were unable to access our services. The root cause was not properly testing out all implemented upgrades before pushing to production servers.

## Timeline (all time in GMT + 1)
![](https://www.ncbar.org/wp-content/uploads/2022/02/Timeline-Visual-300x145.png)

| Time (GMT + 1) | Actions |
| -------------- | -------- |
| 9:45 AM | Upgrades implementation begins |
| 10:00AM | Server Outage begins |
| 10:00AM | Pagers alerted on-call team |
| 10:10AM | On-call team acknowledgement |
| 10:15AM | Rollback initiation begins |
| 10:20AM | Successful rollback|
| 10:20AM | Server restart initiated|
| 10:22AM | 100% of traffic back online |

## Root cause
![](https://blog.systemsengineering.com/hs-fs/hubfs/blog-files/Root%20Cause.jpg?width=600&name=Root%20Cause.jpg)

At 9:45am (GMT + 1) server upgrade was initiated across all our production servers without first releasing on our test environments and performing all necessary unit testing. Part of the upgrade been shipped to production server required an authentication from a 3rd party software, this new implementation is not supported on the current version present on our servers which resulted in the downtime experienced. We were able to resolve this quickly by first performing a rollback the severs previous state thereafter upgrading the current version on our servers.

## Preventive measures
![](https://cdn-ccchn.nitrocdn.com/eoxXytShChgscESECFYcqdYPaOaOGMwn/assets/images/optimized/rev-fbc0c0e/wp-content/uploads/2021/06/prevent-incidents.png)

- Pushing all intended changes 1st to our test environments before shipping to life server.
- Increase the performance metrics threshold to alert on-call engineers on the event of possible server crash 
