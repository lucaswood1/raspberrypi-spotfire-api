# raspberrypi-spotfire-api
Retrieved temperature data and posted to a well's casing temperature

Initially posted on [DataShopTalk.com](https://datashoptalk.com/real-time-production-in-petro-ai-using-raspberry-pi/)

One of the most pressing topics for data administrators is “what can I do with my real-time production data?”. With the advent of science pads and a move to digitization in the oilfield, streaming data has become one of the most valuable assets. But it can take some practice and getting used to.

I enjoyed tinkering around with the Petro.ai platform and while we have simulated wells: it’s much more fun to have some real data. Ruths.ai doesn’t own any wells but when the office got cold brew, I saw the opportunity.

We would connect a Raspberry Pi with a sensor for temperature to the cold brew keg and pipe temperature readings directly into the Petro.ai database. The data would come in as “casing temperature” and we’d be able to watch our coffee machine in real-time using Petro.ai!

## The Plan
The over diagram would look like this:

![diagram](https://datashoptalk.com/wp-content/uploads/2019/06/061019_1640_RealtimePro2.png)

The keg would be connected to the sensor and pass real-time information to the Raspberry Pi. Then it would shape it into the real-time schema and publish to the REST API endpoint.

## Build out
The first step was to acquire the Raspberry Pi. I picked up a relatively inexpensive one off Amazon and then separately purchased two temperature sensors by Adafruit. It read temperature and humidity, but for the moment we’d just use the former.

There’s enough information online to confirm that these would be compatible. After unpacking it, I setup an Ubuntu image and booted it up.
