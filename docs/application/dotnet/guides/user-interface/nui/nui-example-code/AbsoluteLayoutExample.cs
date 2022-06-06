using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace Examples.AbsoluteLayoutExample
{
    public partial class AbsoluteLayoutExample : ContentPage
    {
        public AbsoluteLayoutExample()
        {
            View absoluteLayoutView = new View
            {
                WidthSpecification = LayoutParamPolicies.MatchParent,
                HeightSpecification = LayoutParamPolicies.MatchParent,
                BackgroundColor = Color.White,
            };

            absoluteLayoutView.Layout = new AbsoluteLayout();

            TextLabel header = new TextLabel
            {
                Text = "Stylish Header",
                PointSize = 25,
                Position2D = new Position2D(290, 270)
            };

            View redView = new View
            {
                BackgroundColor = Color.Red,
                Position2D = new Position2D(232, 220),
                WidthSpecification = 800,
                HeightSpecification = 5
            };

            View greenView = new View
            {
                BackgroundColor = Color.Green,
                Position2D = new Position2D(232, 208),
                WidthSpecification = 800,
                HeightSpecification = 5
            };

            View blueView = new View
            {
                BackgroundColor = Color.Blue,
                Position2D = new Position2D(242, 200),
                WidthSpecification = 5,
                HeightSpecification = 400
            };

            View magentaView = new View
            {
                BackgroundColor = Color.Magenta,
                Position2D = new Position2D(254, 200),
                WidthSpecification = 5,
                HeightSpecification = 400
            };

            absoluteLayoutView.Add(header);
            absoluteLayoutView.Add(redView);
            absoluteLayoutView.Add(greenView);
            absoluteLayoutView.Add(blueView);
            absoluteLayoutView.Add(magentaView);

            Content = absoluteLayoutView;
        }
    }
}
