const HelloMessage = React.createClass({
    render: function() {

        return <div>Hello {this.props.name} :{this.props.name}</div>;
    }
 });
 ReactDOM.render(<HelloMessage name="John" />, 
     document.getElementById('wow'));

export default HelloMessage; 