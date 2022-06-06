using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace Examples
{
    public partial class GridLayoutExample : ContentPage
    {
        public GridLayoutExample()
        {
            View gridLayoutView = new View
            {
                Layout = new GridLayout
                {
                    Rows = 3,
                    Columns = 2
                },
                WidthSpecification = LayoutParamPolicies.MatchParent,
                HeightSpecification = LayoutParamPolicies.MatchParent,
                BackgroundColor = new Color("#D7D6F5FF"),
                Padding = new Extents(40, 40, 40, 40)
            };

            View box1 = new View
            {
                BackgroundColor = new Color("#2B7BAAFF"),
            };

            GridLayout.SetHorizontalStretch(box1, GridLayout.StretchFlags.ExpandAndFill);
            gridLayoutView.Add(box1);

            View box2 = new View
            {
                BackgroundColor = new Color("#2B7BAAFF"),
            };

            GridLayout.SetHorizontalStretch(box1, GridLayout.StretchFlags.ExpandAndFill);
            gridLayoutView.Add(box2);

            View box3 = new View
            {
                BackgroundColor = new Color("#2B7BAAFF"),
            };

            GridLayout.SetHorizontalStretch(box1, GridLayout.StretchFlags.ExpandAndFill);
            gridLayoutView.Add(box3);

            View box4 = new View
            {
                BackgroundColor = new Color("#2B7BAAFF"),
            };

            GridLayout.SetHorizontalStretch(box1, GridLayout.StretchFlags.ExpandAndFill);
            gridLayoutView.Add(box4);

            Content = gridLayoutView;
        }
    }
}

