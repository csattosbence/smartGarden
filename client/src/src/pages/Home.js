import {
  Line,
  LineChart,
  XAxis,
  YAxis,
} from 'recharts';




const Home = ({data}) => {

  return (
    <div className="Home">
      <LineChart width={500} height={300} data={data}>
        <XAxis dataKey="currentDate"/>
        <YAxis dataKey="temperature"/>
        <Line type="monotone" dataKey="temperature" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default Home;
