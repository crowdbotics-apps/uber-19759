import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen5993948Navigator from '../features/BlankScreen5993948/navigator';
import UserProfile93947Navigator from '../features/UserProfile93947/navigator';
import Maps93928Navigator from '../features/Maps93928/navigator';
import Settings93906Navigator from '../features/Settings93906/navigator';
import Settings93891Navigator from '../features/Settings93891/navigator';
import NotificationList93890Navigator from '../features/NotificationList93890/navigator';
import Maps93889Navigator from '../features/Maps93889/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen5993948: { screen: BlankScreen5993948Navigator },
UserProfile93947: { screen: UserProfile93947Navigator },
Maps93928: { screen: Maps93928Navigator },
Settings93906: { screen: Settings93906Navigator },
Settings93891: { screen: Settings93891Navigator },
NotificationList93890: { screen: NotificationList93890Navigator },
Maps93889: { screen: Maps93889Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
