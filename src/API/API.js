export const getParcels = async () => {
  try {
    const result = await fetch(
      "app-lb-973713544.eu-central-1.elb.amazonaws.com/api"
    );
    let data = await result.json();
    data = JSON.parse(data.body)
    return data;
  } catch (e) {
    console.log(e);
  }
};

