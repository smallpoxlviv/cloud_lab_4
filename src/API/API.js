export const getParcels = async () => {
  try {
    const result = await fetch(
      "http://back-lb-575935166.us-east-2.elb.amazonaws.com:5000/iot"
    );
    let data = await result.json();
    data = JSON.parse(data.body)
    return data;
  } catch (e) {
    console.log(e);
  }
};

