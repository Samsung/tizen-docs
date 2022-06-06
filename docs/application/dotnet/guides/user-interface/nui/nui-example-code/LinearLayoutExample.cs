using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace Examples
{
	public partial class LinearLayoutExample : ContentPage
	{
		public LinearLayoutExample()
		{
			View linearLayoutView = new View
			{
				Layout = new LinearLayout
				{
					LinearOrientation = LinearLayout.Orientation.Horizontal
				},
				WidthSpecification = LayoutParamPolicies.MatchParent,
				HeightSpecification = LayoutParamPolicies.MatchParent,
				BackgroundColor = new Color("#D7D6F5FF"),
				Padding = new Extents(40, 40, 40, 40)
			};

			View box1 = new View
			{
				WidthSpecification = LayoutParamPolicies.MatchParent,
				HeightSpecification = LayoutParamPolicies.MatchParent,
				BackgroundColor = new Color("#2B7BAAFF"),
			};

			linearLayoutView.Add(box1);

			View box2 = new View
			{
				WidthSpecification = LayoutParamPolicies.MatchParent,
				HeightSpecification = LayoutParamPolicies.MatchParent,
				BackgroundColor = new Color("#6B7BAAFF"),
			};

			linearLayoutView.Add(box2);

			View box3 = new View
			{
				WidthSpecification = LayoutParamPolicies.MatchParent,
				HeightSpecification = LayoutParamPolicies.MatchParent,
				BackgroundColor = new Color("#AB7BAAFF"),
			};

			linearLayoutView.Add(box3);

			View box4 = new View
			{
				WidthSpecification = LayoutParamPolicies.MatchParent,
				HeightSpecification = LayoutParamPolicies.MatchParent,
				BackgroundColor = new Color("#EB7BAAFF"),
			};

			linearLayoutView.Add(box4);

			Content = linearLayoutView;
		}
	}
}
