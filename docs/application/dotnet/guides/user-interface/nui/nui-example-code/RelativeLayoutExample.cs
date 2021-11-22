using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace Examples
{
    public partial class RelativeLayoutExample : ContentPage
    {
        public RelativeLayoutExample()
        {
            View relativeLayoutView = new View
            {
                WidthSpecification = LayoutParamPolicies.MatchParent,
                HeightSpecification = LayoutParamPolicies.MatchParent,
                BackgroundColor = Color.White
            };

            relativeLayoutView.Layout = new RelativeLayout();

            View redView = new View
            {
                BackgroundColor = Color.Red
            };

            RelativeLayout.SetLeftRelativeOffset(redView, 0.0f);
            RelativeLayout.SetRightRelativeOffset(redView, 0.1f);
            RelativeLayout.SetTopRelativeOffset(redView, 0.0f);
            RelativeLayout.SetBottomRelativeOffset(redView, 0.1f);

            RelativeLayout.SetFillHorizontal(redView, true);
            RelativeLayout.SetFillVertical(redView, true);

            relativeLayoutView.Add(redView);

            View blueView = new View
            {
                BackgroundColor = Color.Blue,
                WidthSpecification = 200,
                HeightSpecification = 200
            };

            RelativeLayout.SetLeftRelativeOffset(blueView, 1.0f);
            RelativeLayout.SetRightRelativeOffset(blueView, 1.0f);
            RelativeLayout.SetTopRelativeOffset(blueView, 0.0f);
            RelativeLayout.SetBottomRelativeOffset(blueView, 0.0f);

            RelativeLayout.SetHorizontalAlignment(blueView, RelativeLayout.Alignment.End);
            relativeLayoutView.Add(blueView);

            View yellowView = new View
            {
                BackgroundColor = Color.Yellow,
                WidthSpecification = 600,
                HeightSpecification = 600
            };

            RelativeLayout.SetLeftRelativeOffset(yellowView, 0.5f);
            RelativeLayout.SetRightRelativeOffset(yellowView, 0.5f);
            RelativeLayout.SetTopRelativeOffset(yellowView, 0.5f);
            RelativeLayout.SetBottomRelativeOffset(yellowView, 0.5f);

            RelativeLayout.SetHorizontalAlignment(blueView, RelativeLayout.Alignment.Center);
            RelativeLayout.SetVerticalAlignment(blueView, RelativeLayout.Alignment.Center);
            relativeLayoutView.Add(yellowView);

            View greenView = new View
            {
                BackgroundColor = Color.Green
            };

            RelativeLayout.SetLeftTarget(greenView, yellowView);
            RelativeLayout.SetRightTarget(greenView, yellowView);
            RelativeLayout.SetTopTarget(greenView, yellowView);
            RelativeLayout.SetBottomTarget(greenView, yellowView);

            RelativeLayout.SetLeftRelativeOffset(greenView, 0.0f);
            RelativeLayout.SetRightRelativeOffset(greenView, 0.2f);
            RelativeLayout.SetTopRelativeOffset(greenView, 0.0f);
            RelativeLayout.SetBottomRelativeOffset(greenView, 0.2f);

            RelativeLayout.SetFillHorizontal(greenView, true);
            RelativeLayout.SetFillVertical(greenView, true);
            relativeLayoutView.Add(greenView);

            View blackView = new View
            {
                BackgroundColor = Color.Black,
                Margin = new Extents(50, 50, 50, 50)
            };

            RelativeLayout.SetLeftTarget(blackView, greenView);
            RelativeLayout.SetRightTarget(blackView, yellowView);
            RelativeLayout.SetTopTarget(blackView, greenView);
            RelativeLayout.SetBottomTarget(blackView, yellowView);

            RelativeLayout.SetLeftRelativeOffset(blackView, 1.0f);
            RelativeLayout.SetRightRelativeOffset(blackView, 1.0f);
            RelativeLayout.SetTopRelativeOffset(blackView, 1.0f);
            RelativeLayout.SetBottomRelativeOffset(blackView, 1.0f);

            RelativeLayout.SetFillHorizontal(blackView, true);
            RelativeLayout.SetFillVertical(blackView, true);
            relativeLayoutView.Add(blackView);

            this.Content = relativeLayoutView;
        }
    }
}

