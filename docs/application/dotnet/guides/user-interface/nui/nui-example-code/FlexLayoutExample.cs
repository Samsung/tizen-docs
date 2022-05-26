using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace Examples
{
    public partial class FlexLayoutExample : ContentPage
    {
        public FlexLayoutExample()
        {
            View flexLayoutView = new View
            {
                Layout = new FlexLayout
                {
                    Direction = FlexLayout.FlexDirection.ColumnReverse,
                    Justification = FlexLayout.FlexJustification.FlexStart,
                    Alignment = FlexLayout.AlignmentType.FlexEnd
                },
                WidthSpecification = LayoutParamPolicies.MatchParent,
                HeightSpecification = LayoutParamPolicies.MatchParent,
                BackgroundColor = Color.White,
            };

            TextLabel text1 = new TextLabel
            {
                WidthSpecification = 300,
                HeightSpecification = 40,
                BackgroundColor = new Color("#ff0000"),
            };

            flexLayoutView.Add(text1);

            TextLabel text2 = new TextLabel
            {
                WidthSpecification = 300,
                HeightSpecification = 60,
                BackgroundColor = new Color("#aaaaaa"),
            };

            flexLayoutView.Add(text2);

            TextLabel text3 = new TextLabel
            {
                WidthSpecification = 300,
                HeightSpecification = 40,
                BackgroundColor = new Color("#ffff00"),
            };

            flexLayoutView.Add(text3);

            TextLabel text4 = new TextLabel
            {
                WidthSpecification = 300,
                HeightSpecification = 80,
                BackgroundColor = new Color("#00aaff"),
            };

            flexLayoutView.Add(text4);

            TextLabel text5 = new TextLabel
            {
                WidthSpecification = 300,
                HeightSpecification = 40,
                BackgroundColor = new Color("#00ffff"),
            };

            flexLayoutView.Add(text5);

            Content = flexLayoutView;
        }
    }
}
